# J<sup>3</sup>SPM AI

## Features

- [x] Easy all in one AI solution module for Scanning Probe Microscope (SPM).
- [x] Object detection, classification, segmentation, communication.
- [x] SPM data analysis. ([Gwyddion](https://gwyddion.net))
- [x] Data annotation for object detection and segmentation. ([Labelimg](https://github.com/HumanSignal/labelImg)) ([Labelme](https://github.com/labelmeai/labelme))
- [x] Training, inference at high speed with YOLOv5. ([YOLOv5](https://github.com/ultralytics/yolov5))


## Installation

- Install [Anaconda](https://www.anaconda.com/download/success) first. (Don't add Anaconda to my PATH enviroment variable while installing)
- Install windows_cpu or windows_gpu following steps.
### File downloads (*.yml, *.bat)
#### Option 1
  - Download zip file through main page and use *.yml and *.bat file in zip file

#### Option 2
  - Copy *.yml and *.bat files in Installation folder.

 #### The downloaded batch file by Option 2 doesn't run properly due to an encoding issue. To solve this, copy the contents of the batch file into Notepad, and save it with the same name to overwrite the existing batch file.
 
### Windows_CPU (No GPU)

  - Execute "install_cpuyml.bat" in windows.


### Windows_GPU (With GPU from NVIDIA)

 - Execute "install_gpuyml.bat" in windows.

#### *.yml and *.bat files should be in the same folder.

### Gwyddion installation : Manual installation is necessary.

- [Gwyddion download](http://gwyddion.net/download.php)

## Running J3SPM AI
### Option 1
 - Execute "AIrun.bat" anywhere in windows.

### Option 2
 1. Run Anaconda prompt or Anaconda powershell prompt.
 2. Activate environment: Type below command in an Anaconda prompt.  
        
    - conda activate J3SPM_AI_cpu  
    or  
    - conda activate J3SPM_AI_gpu
 3. Change folder:   Type below command in an Anaconda prompt.
   
    - cd C:\Users\ %USERPROFILE% \J3SPM_AI_cpu\yolov5_J3SPM   (%USERPROFILE%=> windows login name.)  
   or  
    - cd C:\Users\ %USERPROFILE% \J3SPM_AI_gpu\yolov5_J3SPM   (%USERPROFILE%=> windows login name.)  
    
 4. Run `python J3SPM_AI.py` : Type below command in an Anaconda Prompt.
   
    - python J3SPM_AI.py

## YOLOv5 Segmentation model download 
Object detection models of YOLOv5 are downloaded automatically to "yolov5_J3SPM/models" folder at the first inference.
But segmentation models should be downloaded manually before using at [YOLOv5 segmentation] https://github.com/ultralytics/yolov5/discussions/10258).

## Example movies
- [Gwyddion in J3SPM AI](https://youtu.be/Wx5QTSIW67k)
- [Data Labeling in J3SSPM AI](https://youtu.be/2zr7aIva0Sg)
- [Training model in J3SPM AI](https://youtu.be/vnacNW7F0hE)
- [Inference & Zoom scan in J3SPM AI](https://youtu.be/Fy-IjJs9J2w)

## Acknowledgement

Part of Paper: 
