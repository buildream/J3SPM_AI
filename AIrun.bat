@echo off
setlocal EnableExtensions EnableDelayedExpansion

:: ==============================================================
:: CONFIG
:: ==============================================================
set "workdir_cpu=%UserProfile%\J3SPM_AI_cpu\yolov5_J3SPM"
set "workdir_gpu=%UserProfile%\J3SPM_AI_gpu\yolov5_J3SPM"
set "entry=J3SPM_AI.py"

echo.
echo Activating Conda environment:
echo.

:: ==============================================================
:: Initialize Conda (Anaconda or Miniconda)
:: ==============================================================
set "ACTIVATE_BAT=%UserProfile%\anaconda3\Scripts\activate.bat"
if not exist "%ACTIVATE_BAT%" set "ACTIVATE_BAT=%UserProfile%\miniconda3\Scripts\activate.bat"
if not exist "%ACTIVATE_BAT%" (
  echo [ERROR] Could not find conda activate.bat under %%UserProfile%%\anaconda3 or %%UserProfile%%\miniconda3
  echo Please adjust the path to your Conda installation.
  goto :end
)

call "%ACTIVATE_BAT%" >nul 2>&1
if errorlevel 1 (
  echo [ERROR] Failed to initialize conda.
  goto :end
)

:: ==============================================================
:: Discover ONLY the allowed environments
::   - J3SPM_AI_gpu
::   - J3SPM_AI_cpu
:: ==============================================================
set "HAS_GPU="
set "HAS_CPU="
for /f "tokens=1" %%E in ('conda env list ^| findstr /R "^[A-Za-z0-9._-]"') do (
  if /I "%%E"=="J3SPM_AI_gpu" set "HAS_GPU=1"
  if /I "%%E"=="J3SPM_AI_cpu" set "HAS_CPU=1"
)

if not defined HAS_GPU if not defined HAS_CPU (
  echo [ERROR] Neither "J3SPM_AI_gpu" nor "J3SPM_AI_cpu" was found.
  echo Please create one of these environments first.
  goto :end
)

if defined HAS_GPU if not defined HAS_CPU (
  set "TARGET_ENV=J3SPM_AI_gpu"
  set "workdir=!workdir_gpu!"
  goto :have_env
)

if defined HAS_CPU if not defined HAS_GPU (
  set "TARGET_ENV=J3SPM_AI_cpu"
  set "workdir=!workdir_cpu!"
  goto :have_env
)

:: If both exist, ask the user to choose
echo Available environments:
echo   1) J3SPM_AI_gpu
echo   2) J3SPM_AI_cpu
echo.
set /p "CHOICE=Select environment number to activate (1/2, default 1): "
if not defined CHOICE set "CHOICE=1"
if "%CHOICE%"=="2" (
  set "TARGET_ENV=J3SPM_AI_cpu"
  set "workdir=!workdir_cpu!"
) else (
  set "TARGET_ENV=J3SPM_AI_gpu"
  set "workdir=!workdir_gpu!"
)

:have_env
echo.
echo Activating: "!TARGET_ENV!"
call conda activate "!TARGET_ENV!"
if errorlevel 1 (
  echo [ERROR] Failed to activate "!TARGET_ENV!".
  goto :end
)

:: ==============================================================
:: Check working directory (based on selected environment)
:: ==============================================================
if not defined workdir (
  echo [ERROR] workdir was not set. Please check the environment selection logic.
  goto :end
)

if not exist "!workdir!" (
  echo [ERROR] Working directory not found: "!workdir!"
  echo Please confirm the folder exists:
  echo   - "!workdir_cpu!"
  echo   - "!workdir_gpu!"
  goto :end
)
cd /d "!workdir!"

:: ==============================================================
:: Run the program
:: ==============================================================
echo.
echo Running: python "%entry%"
python "%entry%"
set "RC=%ERRORLEVEL%"

:end
echo.
echo [DONE] Exit code: %RC%
pause
exit /b %RC%
