# J<sup>3</sup>SPM AI

## Features

- [x] Easy all in one AI solution module for Scanning Probe Microscope (SPM).
- [x] Object detection, classification, segmentation, communication.
- [x] SPM data analysis. ([Gwyddion](https://gwyddion.net))
- [x] Data annotation for object detection and segmentation. ([Labelimg](https://github.com/HumanSignal/labelImg)) ([Labelme](https://github.com/labelmeai/labelme))
- [x] Training, inference at high speed with YOLOv5. ([YOLOv5](https://github.com/ultralytics/yolov5))


## Installation

- Platform specific installation: [Windows for CPU](#windows_CPU),  [Windows for GPU](#windows_GPU)
- Make "AI_project" folder in your PC and proceed with the installation there. (ex. C:/users/AI_project )
- 

### Windows_CPU

Install [Anaconda](https://https://www.anaconda.com/download/success), then in an Anaconda Prompt and the "AI_project" folder run:

```bash
# create anaconda environment
conda create -n J3SPM_AI_cpu python=3.9.19
conda activate J3SPM_AI_cpu

# install pytorch for cpu
conda install pytorch torchvision torchaudio cpuonly -c pytorch

# install J3SPM_AI
git clone https://github.com/buildream/J3SPM_AI

#install git and clone yolov5
conda install git
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

# install AI tools
conda install -c conda-forge pyqt=5
pip install labelimg
conda install -c conda-forge labelme
conda install pyserial

```

### Windows_GPU

Install [Anaconda](https://https://www.anaconda.com/download/success), then in an Anaconda Prompt and the "AI_project" folder run:

```bash
conda create -n J3SPM_AI_gpu python=3.9.19
conda activate J3SPM_AI_gpu
# install drivers for gpu 
conda install -c conda-forge cudatoolkit=11.8
conda install -c conda-forge cudnn
# intall pytorch for gpu, refer pytorch official website : https://pytorch.org/
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# install J3SPM_AI
git clone https://github.com/buildream/J3SPM_AI

#install git and clone yolov5
conda install git
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

# install AI tools
conda install -c conda-forge pyqt=5
pip install labelimg
conda install -c conda-forge labelme
conda install pyserial

```
### Gwyddion installation

[Gwyddion download](http://gwyddion.net/download.php)

## Usage

Run `python J3SPM_AI.py` in an Anaconda Prompt.
(ex. (J3SPM_AI_CPU) C:\users\AI_project\J3SPM_AI\python J3SPM_AI.py)

## YOLOv5 Segmentation model download 
Object detection models of YOLOv5 are downloaded automatically to "yolov5/models" folder at the first inference.
But segmentation models should be downloaded manually before using at [YOLOv5 segmentation] https://github.com/ultralytics/yolov5/discussions/10258)

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
