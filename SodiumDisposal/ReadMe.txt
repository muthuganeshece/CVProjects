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
- Annotate images in Roboflow
- Train the Yolo model in Google Colab
- Download the model and Apply Inferencing
- Build video with set of input and segmented images


/********* GeM Boards ***********/

Jetson Nano J1010: https://mkp.gem.gov.in/graphics-card/jetson-nano-j1010-edge-ai-module-1252359/p-5116877-47967038554-cat.html#

Jetson Nano B1: https://mkp.gem.gov.in/graphics-card/jetson-nano-b01-module-637300/p-5116877-35096892894-cat.html

Jetson Xavier NX: 
https://mkp.gem.gov.in/graphics-card/jetson-xavier-nx-8gb-module-1252361/p-5116877-6654250441-cat.html#variant_id=5116877-6654250441
https://mkp.gem.gov.in/graphics-card/jetson-xavier-nx-16-gb-module-1252362/p-5116877-16778792483-cat.html#variant_id=5116877-16778792483

Jetson Orin Nano: https://mkp.gem.gov.in/graphics-card/nvidia-jetson-orin-nano-developer-kit-1535351/p-5116877-25845498928-cat.html#variant_id=5116877-25845498928


/**************** Accessories ***************/
- Jetson Orin Nano 8GB Developer kit: https://tannatechbiz.com/nvidia-jetson-orin-nano-developer-kit.html?srsltid=AfmBOooq_8OloL13cWX8jpBevXLt4lEZ67qqEhBkaj3PLukbqQ9plCH3
	- A2 rated 64 GB micro SD card : SanDisk Extreme Pro microSDXC UHS-I (V30, A2)
	- Pre installed with Jetpack SDK
- Display port to HDMI Converter: https://blacki.co.in/products/dptohdmi?srsltid=AfmBOopxHRnqeixVvHYoXONZfdkTaoR7rW8eIpBYY8vsowbFVKeXOcJu
- HDMI cable of length 1 meter: 2 nos.
- 8 channel Relay board with case
- Metal case with antenna: https://hubtronics.in/jetson-orin-case-a


Solid sodium 30kg has been disposed using water mist injection technique in SOCA facility in batches of 4kg each run.
In order to fully automate and speed up the process, a computer vision based water mist injection control system is being developed. 
Identifying the fire and the hydrogen explosions are crucial to effectively control the mist injection.
A deep convolutional neural network (dCNN) model is developed and trained that effectively segments the fire region from the raw image. 
In addition to that, the images are transformed into their corresponding top-view representation using homography techniques for better visualisation.
Currently, a machine learning model is being built to detect hydrogen explosions during the mist injection, which is a critical step in ensuring the timely activation or deactivation of the water mist system
