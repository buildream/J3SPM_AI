@echo off
:: Get the directory where the batch file is located
SET "script_path=%~dp0"
cd /d %script_path%

:: Ensure Conda is properly initialized (adjust the path if necessary)
call "%UserProfile%\anaconda3\Scripts\activate.bat" base

:: GPU 환경이 있는지 확인
conda env list | findstr /c:"J3SPM_AI_gpu" >nul
if %errorlevel%==0 (
    set "env_name=J3SPM_AI_gpu"
    goto ActivateAndRun
)

:: CPU 환경이 있는지 확인
conda env list | findstr /c:"J3SPM_AI_cpu" >nul
if %errorlevel%==0 (
    set "env_name=J3SPM_AI_cpu"
    goto ActivateAndRun
)

:: 환경이 없을 경우 오류 출력 후 종료
echo Error: No J3SPM_AI_gpu or J3SPM_AI_cpu environment exists.
pause
exit /b

:ActivateAndRun
:: Activate the selected environment
echo Activating Conda environment: %env_name%
call conda activate %env_name%

:: Change to the working directory
cd /d "%UserProfile%\%env_name%\yolov5_J3SPM"

:: Keep the console open to inspect any output or errors
python J3SPM_AI.py

