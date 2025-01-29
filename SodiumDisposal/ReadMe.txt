/********** Installations *********/
- pip install ultralytics==
- copy file libomp140.x86_64.dll : Free .DLL download. (dllme.com)
- pip install torch==2.2.2 torchvision==0.17.2 torchaudio
- pip install onnx==1.16.1
- pip install onnxruntime
- pip install openvino


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
	- Create features, No. of contours, Centroid of each contour and Area of each contour
- Find Contours:
	- cv.findcontours used to find the edges of the inferred segmented images
- Find Centroid:
	- Centroid Calculation Algorithm


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


Solid sodium 30kg has been disposed using water mist injection technique in SOCA facility in batches of 4kg each run.
In order to fully automate and speed up the process, a computer vision based water mist injection control system is being developed. 
Identifying the fire and the hydrogen explosions are crucial to effectively control the mist injection.
A deep convolutional neural network (dCNN) model is developed and trained that effectively segments the fire region from the raw image. 
In addition to that, the images are transformed into their corresponding top-view representation using homography techniques for better visualisation.
Currently, a machine learning model is being built to detect hydrogen explosions during the mist injection, which is a critical step in ensuring the timely activation or deactivation of the water mist system

