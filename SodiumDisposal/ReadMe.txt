
/********** Installations *********/
- pip install ultralytics== (8.0.196 for 28_08_2024 model or 8.2.103 for 11_04_2025 model)
- pip install lap
- pip install cython
- pip install bytetracker
- copy file libomp140.x86_64.dll : Free .DLL download. (dllme.com)
- pip install torch==2.2.2 torchvision==0.17.2 torchaudio
- pip install onnx==1.16.1
- pip install onnxruntime
- pip install openvino
- pip install cython

/********** Reference Image ********/
Size: 640 X 640
Layout: Created in same directory


/********** Steps *****************/
- Extract images from videos using fps=3 and resize the image to 640x640
- Annotate images in Roboflow
- Train the Yolo model in Google Colab
- Download the model and Apply Inferencing
- Build video with set of input and segmented images

- Feature Extraction:
	- No. of contours, Centroid of each contour and Area of each contour
- Find Contours:
	- cv.findcontours used to find the edges of the inferred segmented images
- Find Centroid:
	- Centroid Calculation Algorithm

/********* Status ****************/
4 Apr 2025:
- Annotation completed in Roboflow 
- New Dataset version created for (1661 images)

11 Apr 2025:
- Trained YOLOV8 Model on the dataset (1661 images)
- Results are stored in GitHub

04 June  2025:
- Performance of 11_04_2025 model seems to be better, still map50 analysis is required

05 June 2025:
- Tracking Parameters tuning:
	- 04_11_04_2025_Track1: bytetrack.yaml
	- 04_11_04_2025_Track2: 
		- custom_bytetrack.yaml, 
		- track_high_thresh: 0.25, match_thresh: 0.8
	- 04_11_04_2025_Track3: 
		- track_high_thresh: 0.5, match_thresh: 0.5
		
	- 04_11_04_2025_Track4: 
		- track_high_thresh: 0.7, match_thresh: 0.5
	- 04_11_04_2025_Track5: 
		- track_high_thresh: 0.5, match_thresh: 0.3
/*************** Structured Data ***********/
- Video File Name
- Frame
- Feature List:
	- Frame ID
	- Time
	- No. of contours
	- Contour ID
	- Centroid of each contour: List of List
	- Area of each contour: List
	- Confidence of each contour: List
	- Strength of each contour: List
	- Bounding box area: List
	- Bounding box dimension: List of List
	- Bounding box centroid: List of List
	- Visibility level
	
	
/************* EDA ***********/
- Average distance between centroids
- Average strength of mask
- Average bounding box area
- Diff between mean centroid distance between frames

	340100004230121


For the purchase of the following items:1. Wire Stripper - 5 2. Insulation Tape - 30 3. Scissor - 3 4. Tester - 5 5. Measurement Tape (3m) - 4 6. AAA Battery - 20 7. AA Battery - 20 8. 230V 3 core Power cord -  20 9. Knife Blade set - 2 10. 5A/15A/20A Plug Top - 20 each 11. Cable Tie 100mm/150mm/300mm - 2 each 12. Cutting Plier - 2 13. Hacksaw blade - 10 14. Masking Tape - 2 15. Double sided tape - 2 16. Nose Plier - 3 17. Soldering flux - 1 18. Soldering Iron - 2 19. Allen Key set - 1 

/********* GeM Boards ***********/

Jetson Nano J1010: https://mkp.gem.gov.in/graphics-card/jetson-nano-j1010-edge-ai-module-1252359/p-5116877-47967038554-cat.html#

Jetson Nano B1: https://mkp.gem.gov.in/graphics-card/jetson-nano-b01-module-637300/p-5116877-35096892894-cat.html

Jetson Xavier NX: 
https://mkp.gem.gov.in/graphics-card/jetson-xavier-nx-8gb-module-1252361/p-5116877-6654250441-cat.html#variant_id=5116877-6654250441
https://mkp.gem.gov.in/graphics-card/jetson-xavier-nx-16-gb-module-1252362/p-5116877-16778792483-cat.html#variant_id=5116877-16778792483

Jetson Orin Nano: https://mkp.gem.gov.in/graphics-card/nvidia-jetson-orin-nano-developer-kit-1535351/p-5116877-25845498928-cat.html#variant_id=5116877-25845498928


/**************** Accessories ***************/
- Jetson Orin Nano 8GB Developer kit: https://tannatechbiz.com/nvidia-jetson-orin-nano-developer-kit.html?srsltid=AfmBOooq_8OloL13cWX8jpBevXLt4lEZ67qqEhBkaj3PLukbqQ9plCH3
https://robu.in/product/nvidia-jetson-orion-nano-developer-kit/
	- A2 rated 128 GB micro SD card : SanDisk Extreme Pro microSDXC UHS-I (V30, A2)
	- Pre installed with Jetpack SDK
- Display port to HDMI Converter: https://blacki.co.in/products/dptohdmi?srsltid=AfmBOopxHRnqeixVvHYoXONZfdkTaoR7rW8eIpBYY8vsowbFVKeXOcJu
- HDMI cable of length 1 meter: 2 nos.
- 8 channel Relay board : https://robu.in/product/5v-8-channel-ssr-g3mb-202p-solid-state-relay-module-240v-2a-output-resistive-fuse/
- Metal case with antenna: https://hubtronics.in/jetson-orin-case-a
- Power Adapter: 19V 2A with DC Barrel Jack                               

Interface TFT:
https://jetsonhacks.com/2020/05/04/spi-on-jetson-using-jetson-io/

/*************************** Orin Nano Installation ***********************/
Install Deepstream SDK
- sudo apt install deepstream-6.4
- deepstream-app --version-all

Install VS Code
