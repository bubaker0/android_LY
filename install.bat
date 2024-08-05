@echo off
REM تحميل Android SDK Platform Tools
curl -O https://dl.google.com/android/repository/platform-tools-latest-windows.zip
powershell -command "Expand-Archive platform-tools-latest-windows.zip -DestinationPath ."
move platform-tools C:\platform-tools
del platform-tools-latest-windows.zip

REM إضافة ADB إلى مسار النظام (PATH)
setx PATH "%PATH%;C:\platform-tools"