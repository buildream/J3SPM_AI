@echo off
:: Get the directory where the batch file is located
SET "script_path=%~dp0"
cd /d %script_path%


:: Ensure Conda is properly initialized (adjust the path if necessary)
call "%UserProfile%\anaconda3\Scripts\activate.bat" base

:: Check if the folder exists, if not, create it
if not exist "C:\Users\J3SPM_AI_gpu" (
    mkdir "C:\Users\J3SPM_AI_gpu"
)

:: 환경이 이미 존재하는지 확인합니다.
conda env list | findstr "J3SPM_AI_gpu" >nul
if %errorlevel%==0 (
    echo Enviroment aleary exist so activate it and go to next process.
    goto ActivateEnvironment
)


:: Create the environment using the YAML file
echo Creating the Conda environment...
call conda env create -f "%script_path%environment_gpu.yml"

:: Ensure the script waits for the environment creation to complete
if %errorlevel% neq 0 (
    echo Error: Failed to create the Conda environment.
    pause
    exit /b %errorlevel%
)

:: 환경 생성 후, 배치 파일을 다시 실행합니다.
echo Environment created, restart batch file.
pause
cmd /c "%script_path%install_gpuyml.bat"

: ActivateEnvironment
call conda activate J3SPM_AI_gpu

:: Change to the working directory
cd /d "C:\Users\J3SPM_AI_gpu"

:: Clone the J3SPM AI repository
git clone https://github.com/buildream/J3SPM_AI.git 

:: Clone the YOLOv5 repository
git clone https://github.com/ultralytics/yolov5.git

:: Change directory to yolov5
cd yolov5

:: Install pip requirements
pip install -r requirements.txt

:: Further setup commands (optional)
cd ..\J3SPM_AI

:: move files
move *.py "C:\Users\J3SPM_AI_gpu\yolov5"
move resource.qrc "C:\Users\J3SPM_AI_gpu\yolov5"
move testimg.jpg "C:\Users\J3SPM_AI_gpu\yolov5"

cd ..\yolov5

echo Intallment completed!!  Type "python J3SPM_AI.py" to run program.
echo If you meet PyQT related error, restart console.

:: Keep the console open to inspect any output or errors
pause
cmd





