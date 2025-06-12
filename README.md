# J<sup>3</sup>SPM AI

## Features

- [x] Easy all in one AI solution module for Scanning Probe Microscope (SPM).
- [x] Object detection, classification, segmentation, communication.
- [x] SPM data analysis. ([Gwyddion](https://gwyddion.net))
- [x] Data annotation for object detection and segmentation. ([Labelimg](https://github.com/HumanSignal/labelImg)) ([Labelme](https://github.com/labelmeai/labelme))
- [x] Training, inference at high speed with YOLOv5. ([YOLOv5](https://github.com/ultralytics/yolov5))


## Installation

- Install [Anaconda](https://www.anaconda.com/download/success) or [miniconda](https://www.anaconda.com/download/success) first.
- Install windows_cpu or windows_gpu following steps.

### Windows_CPU

Copy `enviroment_cpu.yml` and `install_cpuyml.bat` files in `Installment` folder to your computer.  
(ex. C:\Users\ %USERPROFILE% \cpu_install , %USERPROFILE%=> windows login name)


### Windows_GPU

Copy `enviroment_gpu.yml` and `install_gpuyml.bat` files in `Installment` folder to your computer.  
(ex. C:\Users\ %USERPROFILE% \gpu_install , %USERPROFILE%=> windows login name)


### Gwyddion installation

[Gwyddion download](http://gwyddion.net/download.php)

## Usage
1. Run Anaconda prompt or Anaconda powershell prompt.
2. Activate environment: Type below command in an Anaconda prompt.  
        
    conda activate J3SPM_AI_cpu  
    or  
    conda activate J3SPM_AI_gpu
3. Change folder:   Type below command in an Anaconda prompt.
   
   cd C:\Users\ %USERPROFILE% \J3SPM_AI_cpu\yolov5_J3SPM   (%USERPROFILE%=> windows login name.)  
   or  
   cd C:\Users\ %USERPROFILE% \J3SPM_AI_gpu\yolov5_J3SPM   (%USERPROFILE%=> windows login name.)  
    
4. Run `python J3SPM_AI.py` : Type below command in an Anaconda Prompt.
   
    python J3SPM_AI.py

## YOLOv5 Segmentation model download 
Object detection models of YOLOv5 are downloaded automatically to "yolov5_J3SPM/models" folder at the first inference.
But segmentation models should be downloaded manually before using at [YOLOv5 segmentation] https://github.com/ultralytics/yolov5/discussions/10258).

# Tutorial 
cd examples/tutorial

## Examples

* [Image Classification](examples/classification)
* [Bounding Box Detection](examples/bbox_detection)
* [Semantic Segmentation](examples/semantic_segmentation)
* [Instance Segmentation](examples/instance_segmentation)
* [Video Annotation](examples/video_annotation)

## Acknowledgement

Part of Paper: 
