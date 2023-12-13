@echo off

REM This script is used to install the dependencies for the program

REM Packages to install
set packages=windows-curses, colored

REM Check if python3 is already installed
where python3 >nul 2>nul
if %errorlevel% equ 0 (
    echo Python3 is already installed
) else (
    echo Install Python3 from the Microsoft Store or from the python website at https://www.python.org
)

REM Install packages
if defined packages[0] (
    for %%p in (%packages%) do (
        pip install %p
    )
) else (
    echo No packages needed to install
)
