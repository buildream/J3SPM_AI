# J<sup>3</sup>SPM AI

## Features

- [x] Easy all in one AI solution module for Scanning Probe Microscope (SPM).
- [x] Object detection, classification, segmentation, communication.
- [x] SPM data analysis. ([Gwyddion](https://gwyddion.net))
- [x] Data annotation for object detection and segmentation. ([Labelimg](https://github.com/HumanSignal/labelImg)) ([Labelme](https://github.com/labelmeai/labelme))
- [x] Training, inference at high speed with YOLOv5. ([YOLOv5](https://github.com/ultralytics/yolov5))


## 🖥️ Installation 
### If you encounter issues during training or inference, please clone the repository again and reinstall it. This applies to installations performed on or after July 6, 2026.
### **⚠️ Note:** Please remove any previously installed J3SPM_AI folders and backup your works before reinstalling.
>
>#### ⚠️ Tip: Easy update
>    → Download the latest "J3SPM_AI.py" and "J3SPM_AI_GUI.py", then replace the existing files in your "yolov5_J3SPM" folder.
### 1. Install Dependencies  
- Install [Anaconda](https://www.anaconda.com/download/success) first.
>⚠️ Please install **Anaconda (not Miniconda)**.
>
>⚠️ *Do NOT add Anaconda to the PATH environment variable during installation.*
>
### 2. Download Installation Files  
YAML files (`*.yml`) and batch files (`*.bat`) are required.

#### Option 1 (recommended)
1. Download Zip from the GitHub main page.
2. Unzip → the installation folder will contain `*.yml` and `*.bat` files.

#### Option 2
1. Copy the contents of the YAML and BAT files from GitHub.  
2. Create new `*.yml` / `*.bat` files manually on your computer.

> ⚠️ Batch files created manually may not run due to encoding issues.  
> To fix: open the `.bat` file in Notepad → re-save with the same name.

>
### 3. Installation

#### Option 1: Windows_CPU (No GPU)

  - Run "install_cpuyml.bat" in windows.


#### Option 2: Windows_GPU (With GPU from NVIDIA)

 - Run "install_gpuyml.bat" in windows.

>  You can install both options if you have GPU.
> 
>  ⚠️ `*.yml` and `*.bat` files **must be in the same folder**.
 

#### Gwyddion Installation (Manual)
- Download from:  
 👉 http://gwyddion.net/download.php

>
## ▶️ Running J<sup>3</sup>SPM AI
### **Option 1 (Simple)**
 - Run "AIrun.bat" in "J3SPM_AI" folder.  (C:\Users\ %USERPROFILE% \J3SPM_AI_cpu or gpu\J3SPM_AI)

### **Option 2 (Manual Execution)**
 1. Run Anaconda prompt or Anaconda powershell prompt.
 2. Activate environment: Type below command in an Anaconda prompt.  
        
    - conda activate J3SPM_AI_cpu  
    or  
    - conda activate J3SPM_AI_gpu
 3. Change folder:   Type below command in an Anaconda prompt.
   
    - cd C:\Users\ %USERNAME% \J3SPM_AI_cpu\yolov5_J3SPM   (%USERPNAME%=> windows login name.)  
   or  
    - cd C:\Users\ %USERPNAME% \J3SPM_AI_gpu\yolov5_J3SPM   (%USERNAME%=> windows login name.)  
    
 4. Run `python J3SPM_AI.py` : Type below command in an Anaconda Prompt.
   
    - python J3SPM_AI.py

#### 📥 YOLOv5 Model Download
The default YOLOv5 segmentation and detection models are automatically downloaded 
to the `yolov5_J3SPM` folder the **first time you run inference**.


## 🎬 Example Movies
- [Install and basic test](https://youtu.be/zuVcmX59AxM)
- [Gwyddion in J<sup>3</sup>SPM AI](https://youtu.be/Wx5QTSIW67k)
- [Dataset preparation for training in J<sup>3</sup>SPM AI](https://youtu.be/dSb8vSxUbJc)
- [Data Labeling for obeject detection and segmentation in J<sup>3</sup>SPM AI](https://youtu.be/2zr7aIva0Sg)
- [Training model in J<sup>3</sup>SPM AI](https://youtu.be/vnacNW7F0hE)
- [Inference & Zoom scan in J<sup>3</sup>SPM AI with DVD fit length AI model](https://youtu.be/zgs247gm3BY)
- [Inference & Zoom scan in J<sup>3</sup>SPM AI with common object AI model](https://youtu.be/Fy-IjJs9J2w)

- [Training YOLOv5 model in Google colab](https://youtu.be/YfryRAA26ZE)

## 📑 Acknowledgement
Part of this work is described in the following paper:

S. Lee, **"J³SPM AI: An Integrated Open-Source Platform for AI-Assisted Image Analysis and Image-Guided Workflows in Scanning Probe Microscopy,"**  *Micron*, 2026.  DOI: https://doi.org/10.1016/j.micron.2026.104017
## 📢 **Questions or issues?**  
Please use the [Issues](https://github.com/buildream/J3SPM_AI/issues) or [Discussions](https://github.com/buildream/J3SPM_AI/discussions) tabs.

