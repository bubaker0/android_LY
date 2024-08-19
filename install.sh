#!/bin/bash

# تحميل Android SDK Platform Tools
wget https://dl.google.com/android/repository/platform-tools-latest-darwin.zip
unzip platform-tools-latest-darwin.zip
sudo mv platform-tools /usr/local/bin/
rm platform-tools-latest-darwin.zip

# إضافة ADB إلى مسار النظام (PATH)
echo 'export PATH=$PATH:/usr/local/bin/platform-tools' >> ~/.bash_profile

# تطبيق التغييرات
source ~/.bash_profile