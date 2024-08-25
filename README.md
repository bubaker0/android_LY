# خطوات تثبيت متطلبات البرنامج **Android_LY**

### 1. تحقق من وجود Python
تأكد من أنك قمت بتثبيت Python على جهازك. افتح سطر الأوامر (Command Prompt) واكتب:

```bash
python --version
```

إذا لم يكن مثبتًا، يمكنك تنزيله من [الموقع الرسمي](https://www.python.org/downloads/).

### 2. تثبيت المتطلبات باستخدام `requirements.txt`
افتح سطر الأوامر وانتقل إلى مجلد البرنامج باستخدام الأمر:

```bash
cd \Android_LY
```

ثم قم بتثبيت المتطلبات بكتابة:

```bash
pip install -r requirements.txt
```

### 3. استخدام `install.bat` أو `install.sh`
يمكنك استخدام السكربتات المرفقة لتسهيل التثبيت:

- **لنظام Windows**: انقر مزدوجًا على `install.bat` أو استخدم سطر الأوامر:

  ```bash
  install.bat
  ```

- **لنظام Linux/Mac**: استخدم الأمر التالي:

  ```bash
  bash install.sh
  ```

### 4. التأكد من تثبيت ADB
تحقق من وجود ADB (Android Debug Bridge) باستخدام:

```bash
adb version
```

إذا لم يكن مثبتًا، يمكنك تنزيله كجزء من [Android SDK](https://developer.android.com/studio/releases/platform-tools).

### 5. تشغيل البرنامج
بعد تثبيت المتطلبات، يمكنك تشغيل البرنامج بكتابة:

```bash
python main.py
```

### ملاحظات
- تأكد من وجود الأذونات اللازمة لتشغيل البرامج.
- إذا واجهت مشاكل، تحقق من رسائل الخطأ في سطر الأوامر.

---

## شرح عمل البرنامج ودور كل زر


![samsung](https://github.com/user-attachments/assets/1656b8e1-0d59-4189-bd4b-56136ae4a9f8)
### 1. Samsung
- **Reboot**: لإعادة تشغيل الجهاز.
- **Show Accounts**: لعرض معلومات الحسابات الموجودة على الجهاز.
- **Download APK**: لتحميل ملف APK.
- **Serial**: لعرض رقم السيريال للجهاز.
- **Show APK**: لعرض التطبيقات المثبتة على الجهاز.
- **Open App**: لفتح تطبيق معين.
- **Uninstall App**: لإلغاء تثبيت تطبيق.
- **Download Mode**: لدخول وضع التحميل.
- **Recovery Mode**: لدخول وضع الاسترداد.
- **Unlock**: لفتح قفل الشاشة.
- **Updates**: للتحقق من التحديثات المتاحة.
- **Screen Video**: لتسجيل فيديو لشاشة الجهاز.
- **Developer**: لفتح تطبيق TikTok للمطورين.
- **FRP - Android 11**: لتجاوز حماية إعادة ضبط المصنع لأندرويد 11.
- **FRP - Android 13**: لتجاوز حماية إعادة ضبط المصنع لأندرويد 13.
- **Enable ADB**: لتمكين ADB عبر منفذ معين.
```
![oppo](https://github.com/user-attachments/assets/c1277666-cddc-4706-9f08-abddc7b05d62)
### 2. Oppo
- **Reboot**: لإعادة تشغيل الجهاز.
- **Data**: لعرض معلومات البيانات.
- **Download APK**: لتحميل ملف APK.
- **Serial**: لعرض رقم السيريال للجهاز.
- **Show APK**: لعرض التطبيقات المثبتة.
- **Open App**: لفتح تطبيق معين.
- **Uninstall App**: لإلغاء تثبيت تطبيق.
- **Download Mode**: لدخول وضع التحميل.
- **Recovery Mode**: لدخول وضع الاسترداد.
- **Unlock**: لفتح قفل الشاشة.
- **Updates**: للتحقق من التحديثات.
- **Screen Video**: لتسجيل فيديو للشاشة.
- **Developer**: لفتح تطبيق للمطورين.
```
![MTK](https://github.com/user-attachments/assets/c1a2ae35-0bbe-43c9-b71f-c45a90b4494c)
### 3. MTK
- **Bypass Secure Boot**: لتجاوز أمان التمهيد.
- **Format**: لتهيئة بيانات الجهاز.
- **Remove FRP**: لإزالة حماية إعادة ضبط المصنع.
- **Bypass Mi Account**: لتجاوز حساب Xiaomi.
- **Remove Demo**: لإزالة وضع العرض التوضيحي.
- **Unlock Bootloader**: لفتح قفل المحمل.
- **Relock Bootloader**: لإعادة قفل المحمل.
- **Read Flash**: لقراءة محتويات الذاكرة.
- **Write Flash**: لكتابة بيانات إلى الذاكرة.
- **Erase Userdata**: لمسح بيانات المستخدم.
- **Dump BROM**: لتفريغ محتويات Boot ROM.
- **Dump SRAM**: لتفريغ ذاكرة SRAM.
- **Get Target Config**: للحصول على إعدادات الجهاز المستهدف.
## كيفية فتح الملفات بعد استخدام Git LFS

عند استخدام Git LFS، الملفات الكبيرة يتم تخزينها كـ "مؤشرات" داخل المستودع، بينما المحتوى الفعلي يتم تخزينه في نظام LFS. لفتح الملفات بعد تنزيل المستودع:

1. **تأكد من تثبيت Git LFS**:
   تأكد من أنك قد قمت بتثبيت Git LFS على جهازك.

2. **قم بتشغيل الأمر**:
   بعد تنزيل المستودع، استخدم الأمر التالي لتحميل الملفات الكبيرة:
   ```bash
   git lfs pull
