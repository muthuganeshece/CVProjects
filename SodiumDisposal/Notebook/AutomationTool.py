import sys, os, cv2, io
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFileDialog, QLineEdit, QMessageBox, QTextEdit, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import FinalIntegration as fi
import numpy as np


# --- Redirect print statements to GUI log ---
class EmittingStream(io.StringIO):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit

    def write(self, text):
        if text.strip() != "":
            self.text_edit.append(text.strip())
            self.text_edit.verticalScrollBar().setValue(
                self.text_edit.verticalScrollBar().maximum()
            )

    def flush(self):
        pass


class SparkDetectionGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spark Detection - Image Viewer")
        self.setGeometry(200, 100, 1100, 750)

        # --- Image display labels ---
        self.raw_label = QLabel("Raw Image")
        self.mask_label = QLabel("Segmented Mask")
        for label in [self.raw_label, self.mask_label]:
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: 2px solid gray; background-color: #f9f9f9;")
            label.setMinimumSize(400, 300)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # --- Result display fields ---
        self.binary_result = QLineEdit()
        self.binary_result.setPlaceholderText("Binary Result (Yes/No)")
        self.value_result = QLineEdit()
        self.value_result.setPlaceholderText("Value Result (e.g. 0.85)")

        # --- Buttons ---
        self.load_btn = QPushButton("Load Folder")
        self.next_btn = QPushButton("Next Image")
        self.record_btn = QPushButton("Record Result")

        # --- Status log window ---
        self.log_window = QTextEdit()
        self.log_window.setReadOnly(True)
        self.log_window.setFixedHeight(150)
        self.log_window.setPlaceholderText("Status messages will appear here...")
        self.log_window.setStyleSheet("border: 2px solid #666; background-color: #f8f8f8;")

        # --- Layouts ---
        img_layout = QHBoxLayout()
        img_layout.addWidget(self.raw_label)
        img_layout.addWidget(self.mask_label)

        result_layout = QHBoxLayout()
        result_layout.addWidget(self.binary_result)
        result_layout.addWidget(self.value_result)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.load_btn)
        btn_layout.addWidget(self.next_btn)
        btn_layout.addWidget(self.record_btn)

        main_layout = QVBoxLayout()
        main_layout.addLayout(img_layout, stretch=3)
        main_layout.addLayout(result_layout)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.log_window, stretch=1)

        self.setLayout(main_layout)

        # --- Connections ---
        self.load_btn.clicked.connect(self.load_folder)
        self.next_btn.clicked.connect(self.show_next_image)
        self.record_btn.clicked.connect(self.record_result)

        # --- State variables ---
        self.image_files = []
        self.current_index = -1

        # --- Redirect print() to GUI log ---
        sys.stdout = EmittingStream(self.log_window)
        
        self.det_obj = fi.spark_detection()
        self.det_obj.load_models()
        
        print("✅ Application started. Ready to load images.")

    def load_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Image Folder")
        if folder:
            self.image_files = [
                os.path.join(folder, f)
                for f in os.listdir(folder)
                if f.lower().endswith(('.jpg', '.jpeg', '.png'))
            ]
            self.image_files.sort()
            self.current_index = -1
            print(f"📁 Loaded {len(self.image_files)} images from: {folder}")
            QMessageBox.information(self, "Folder Loaded",
                                    f"Loaded {len(self.image_files)} images.")
        else:
            print("⚠️ No folder selected.")
            QMessageBox.warning(self, "Warning", "No folder selected.")

    def show_next_image(self):
        if not self.image_files:
            print("⚠️ No images loaded.")
            QMessageBox.warning(self, "Warning", "No images loaded.")
            return

        self.current_index += 1
        if self.current_index >= len(self.image_files):
            print("ℹ️ End of image list reached.")
            QMessageBox.information(self, "End", "No more images.")
            self.current_index = len(self.image_files) - 1
            return

        img_path = self.image_files[self.current_index]
        print(f"📸 Displaying: {img_path}")
        raw_img = cv2.imread(img_path)
        preprocessed_img = fi.preprocess_image(raw_img)

        if raw_img is None:
            print(f"❌ Failed to read: {img_path}")
            return

        # --- Display raw image ---
        self.display_image(self.raw_label, preprocessed_img)
        
        yolo_results, lstm_result = self.det_obj.inference_image(img_path)
        
        if yolo_results[0].masks is not None:
            masks = np.array(yolo_results[0].masks.data)
            combined_mask = np.any(masks, axis=0).astype(np.uint8)
            combined_mask_3ch = cv2.merge([combined_mask * 255] * 3)
        else:
            combined_mask_3ch = np.zeros((640, 640, 3), dtype=np.uint8)
        
        self.display_image(self.mask_label, combined_mask_3ch)

 
        self.binary_result.setText(str(lstm_result))
        #self.value_result.setText(str(value_output))

        #print(f"Result → Binary: {binary_output}, Value: {value_output}")

    def display_image(self, label, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qimg = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pix = QPixmap.fromImage(qimg)
        label.setPixmap(pix.scaled(label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def record_result(self):
        if self.current_index < 0 or not self.image_files:
            print("⚠️ No image selected for recording.")
            QMessageBox.warning(self, "Warning", "No image selected.")
            return

        img_name = os.path.basename(self.image_files[self.current_index])
        binary_val = self.binary_result.text()
        value_val = self.value_result.text()

        with open("results_log.csv", "a") as f:
            f.write(f"{img_name},{binary_val},{value_val}\n")

        print(f"💾 Recorded result for {img_name}: {binary_val}, {value_val}")
        QMessageBox.information(self, "Saved", f"Recorded result for {img_name}")

    def closeEvent(self, event):
        print("🛑 Closing application.")
        sys.stdout = sys.__stdout__
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SparkDetectionGUI()
    gui.show()
    
    
    
    sys.exit(app.exec_())
