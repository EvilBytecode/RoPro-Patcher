@echo off
py --version > nul 2>&1
if %errorlevel% equ 0 (
    echo [%TIME%]Python is installed. Version:
    py --version
pip install tqdm
pip install plyer
pip install pyautogui
pip install subprocess
pip install zipfile
pause
) else (
    echo Python is not installed, please start PythonInstaller.bat
    pause
    )
