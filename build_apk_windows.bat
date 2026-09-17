@echo off
title Escape Mystery Android Builder
echo ==========================================
echo ESCAPE MYSTERY - ANDROID APK BUILDER
echo ==========================================
echo.
echo This script is for WSL/Linux.
echo First run: wsl --install
echo Then open Ubuntu and go to this project.
echo.
echo Install dependencies:
echo sudo apt update
echo sudo apt install -y python3-pip git zip unzip openjdk-17-jdk
echo pip3 install --user buildozer cython
echo.
echo Build APK:
echo buildozer android debug
echo.
echo Your APK will appear in the bin folder.
pause
