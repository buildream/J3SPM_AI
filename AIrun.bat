@echo off
setlocal enabledelayedexpansion

:: ==============================================================
:: Move to the folder where this batch file lives
:: ==============================================================
SET "script_path=%~dp0"
cd /d "%script_path%"

:: ==============================================================
:: Initialize Conda (adjust the path if your Anaconda location differs)
:: ==============================================================
call "%UserProfile%\anaconda3\Scripts\activate.bat" base

:: ==============================================================
:: Check if GPU / CPU environments exist
:: ==============================================================
set "env_gpu=J3SPM_AI_gpu"
set "env_cpu=J3SPM_AI_cpu"

set "has_gpu="
set "has_cpu="

:: Look for environment names in `conda env list` output
conda env list | findstr /i /c:"%env_gpu%" >nul && set "has_gpu=1"
conda env list | findstr /i /c:"%env_cpu%" >nul && set "has_cpu=1"

:: If neither environment exists, stop here
if not defined has_gpu if not defined has_cpu (
  echo [ERROR] Neither "%env_gpu%" nor "%env_cpu%" exists.
  pause
  exit /b 1
)

:: ==============================================================
:: If both exist, let the user choose; otherwise auto-select
:: ==============================================================
if defined has_gpu if defined has_cpu (
  echo.
  echo Both environments are available. Please choose:
  echo   [1] %env_gpu%  (GPU^) 
  echo   [2] %env_cpu%  (CPU^)
  choice /c 12 /n /m "Select (1/2): "
  if errorlevel 2 set "env_name=%env_cpu%"
  if errorlevel 1 if not defined env_name set "env_name=%env_gpu%"
) else (
  if defined has_gpu set "env_name=%env_gpu%"
  if defined has_cpu set "env_name=%env_cpu%"
)

:: ==============================================================
:: Activate the selected Conda environment
:: ==============================================================
echo.
echo Activating Conda environment: %env_name%
call conda activate "%env_name%" || (
  echo [ERROR] Failed to activate: %env_name%
  pause
  exit /b 1
)

:: ==============================================================
:: Change to working directory for the app
:: NOTE: Adjust the path below if your folder structure is different.
:: ==============================================================
set "workdir=%UserProfile%\%env_name%\yolov5_J3SPM"
if not exist "%workdir%" (
  echo [ERROR] Working directory not found: "%workdir%"
  echo Please update the workdir path near the bottom of this script.
  pause
  exit /b 1
)
cd /d "%workdir%"

:: ==============================================================
:: Run the program and keep the console open afterwards
:: ==============================================================
echo.
echo Running: python J3SPM_AI.py
echo (The console will stay open after exit)
echo.
python J3SPM_AI.py

echo.
echo [DONE] Program exited.
:: pause
exit /b 0
