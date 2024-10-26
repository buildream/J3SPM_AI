# J<sup>3</sup>SPM AI

## Features

- [x] Easy all in one AI solution module for Scanning Probe Microscope (SPM).
- [x] Object detection, classification, segmentation, communication.
- [x] SPM data analysis. ([Gwyddion](https://gwyddion.net))
- [x] Data annotation for object detection and segmentation. ([Labelimg](https://github.com/HumanSignal/labelImg)) ([Labelme](https://github.com/labelmeai/labelme))
- [x] Training, inference at high speed with YOLOv5. ([YOLOv5](https://github.com/ultralytics/yolov5))


## Installation

- Install [Anaconda](https://https://www.anaconda.com/download/success) first.
- Install windows_cpu or windows_gpu.

### Windows_CPU

Copy "enviroment_cpu.yml" and "install_cpuyml.bat" files in "Installment" folder to your computer. (ex. C:\Users\build\cpu_install )
Ensure "install_cpuyml.bat" is being run with administrative privileges. Right-click the batch file and select "Run as administrator".

### Windows_GPU

Copy "enviroment_gpu.yml" and "install_gpuyml.bat" files in "Installment" folder to your computer. (ex. C:\Users\build\gpu_install )
Ensure "install_gpuyml.bat" is being run with administrative privileges. Right-click the batch file and select "Run as administrator".

### Gwyddion installation

[Gwyddion download](http://gwyddion.net/download.php)

## Usage
1. Run Anaconda prompt or Anaconda powershell prompt.
2. Activate J3SPM_AI_cpu or J3SPM_AI_gpu environment ( conda activate J3SPM_AI_cpu ).
3. Change folder ( cd C:\Users\J3SPM_AI_cpu\yolov5 ).
4. Run `python J3SPM_AI.py` in an Anaconda Prompt.
  (ex. (J3SPM_AI_cpu) C:\users\J3SPM_AI_cpu\yolov5\python J3SPM_AI.py)

## YOLOv5 Segmentation model download 
Object detection models of YOLOv5 are downloaded automatically to "yolov5/models" folder at the first inference.
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
