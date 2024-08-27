import tkinter as tk
from tkinter import Text, filedialog, messagebox
from PIL import Image, ImageTk
import os
import subprocess
import threading
import queue
import requests
import re
import webbrowser



class App:
    def __init__(self, root):
        self.root = root
        self.version = "1.1.3"
        self.root.title(f"Android_LY - V{self.version}")
        self.root.geometry("900x600")
        self.root.iconbitmap(r"Img\mobile.ico")
        self.root.configure(bg="#000000")
        self.root.bind("<KeyPress-Escape>", self.exit_program)
        self.root.protocol("WM_DELETE_WINDOW", self.exit_program)
        self.message_queue = queue.Queue()
        self.create_widgets()
        self.device_check_timer = None
        self.is_device_connected = False
        self.check_device()  # بدء عملية التحقق
        self.process_queue()  # بدء معالجة queue
        
    def check_device(self):
        try:
            result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode()

            lines = output.splitlines()
            if len(lines) > 1 and "device" in lines[1]:
                device_line = lines[1].split()
                device_id = device_line[0]
                device_info = f"[MTP] جهاز متصل: {device_id}"

                if not self.is_device_connected:
                    self.is_device_connected = True
                    self.message_queue.put("جهاز متصل تم اكتشافه.")
                else:
                    self.message_queue.put(device_info)

            else:
                if self.is_device_connected:
                    self.is_device_connected = False
                    self.message_queue.put("جهاز متصل تم فصله.")
                else:
                    self.message_queue.put("لا يوجد جهاز متصل.")

        except Exception as e:
            self.message_queue.put("حدث خطأ في الكشف عن الجهاز.")

        self.device_check_timer = threading.Timer(5, self.check_device)
        self.device_check_timer.start()

    def process_queue(self):
        try:
            while True:
                message = self.message_queue.get_nowait()
                self.update_entry(message)
        except queue.Empty:
            pass
        self.root.after(100, self.process_queue)  # استمر في معالجة queue

    def update_entry(self, message):
        self.root.after(0, lambda: self.new_entry.delete(0, tk.END) or self.new_entry.insert(0, message))

    def stop_device_check(self):
        if self.device_check_timer:
            self.device_check_timer.cancel()
        
    def create_widgets(self):
        self.samsung_img = Image.open("img/samsung.png").resize((50, 50))
        self.samsung_img = ImageTk.PhotoImage(self.samsung_img)

        self.oppo_img = Image.open("img/oppo.png").resize((50, 50))
        self.oppo_img = ImageTk.PhotoImage(self.oppo_img)
        
        self.MTK_img = Image.open("img/MTK.png").resize((50, 50))
        self.MTK_img = ImageTk.PhotoImage(self.MTK_img)

        self.top_frame = tk.Frame(self.root, bg="#000000", height=50)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.button_frame = tk.Frame(self.top_frame, bg="#000000")
        self.button_frame.pack(side=tk.TOP, pady=10)

        self.samsung_button = tk.Button(self.button_frame, image=self.samsung_img, text="Samsung", compound=tk.TOP, bg="#333333", fg="#FFFFFF", font=("Arial", 12), command=self.handle_samsung)
        self.samsung_button.pack(side=tk.LEFT, padx=20)

        self.oppo_button = tk.Button(self.button_frame, image=self.oppo_img, text="OPPO", compound=tk.TOP, bg="#333333", fg="#FFFFFF", font=("Arial", 12), command=self.handle_oppo)
        self.oppo_button.pack(side=tk.LEFT, padx=20)
        
        self.MTK_button = tk.Button(self.button_frame, image=self.MTK_img, text="MTK", compound=tk.TOP, bg="#333333", fg="#FFFFFF", font=("Arial", 12), command=self.handle_MTK)
        self.MTK_button.pack(side=tk.LEFT, padx=20)

        self.bottom_frame = tk.Frame(self.root, bg="#000000")
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.bottom_frame1 = tk.Frame(self.bottom_frame, bg="#000000", width=150)
        self.bottom_frame1.pack(side=tk.LEFT, fill=tk.Y)

        self.bottom_frame2 = tk.Frame(self.bottom_frame, bg="#000000")
        self.bottom_frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.bottom_frame3 = tk.Frame(self.bottom_frame, bg="#000000")
        self.bottom_frame3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.bottom_frame4 = tk.Frame(self.bottom_frame, bg="#000000")
        self.bottom_frame4.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.new_entry_label = tk.Label(self.bottom_frame1, text="USB", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.new_entry_label.pack(pady=(10, 5))
    
        self.new_entry = tk.Entry(self.bottom_frame1, bg="#444444", fg="#FFFFFF", font=("Arial", 10),justify='center')
        self.new_entry.pack(fill='x', padx=10, pady=(0, 10))
    
        self.text = Text(self.bottom_frame1, wrap='word', bg="#1C1C1C", font=("Arial", 10), fg="#FFFFFF")
        self.text.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        self.create_buttons()
        
    
    
    def remove_lock(self):

        try:
            # التأكد من أن الجهاز متصل

            result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode()
            if "device" in output:
                # الدخول إلى وضع الاسترداد
                os.system("adb reboot recovery")
                # تنفيذ الأوامر لإزالة القفل
                os.system("adb shell rm /data/system/gesture.key")
                os.system("adb shell rm /data/system/locksettings.db")
                self.text.insert(tk.END, "تمت إزالة القفل بنجاح.\n")
            else:
                self.text.insert(tk.END, "لا يوجد جهاز متصل.\n")
        except Exception as e:
            self.text.insert(tk.END, f"حدث خطأ: {e}\n")


    def create_buttons(self):
        self.hint_label = tk.Label(self.bottom_frame2, text="ادخل اسم تطبيق:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.hint_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        self.entry = tk.Entry(self.bottom_frame2 , bg="#444444", fg="#FFFFFF")
        self.entry.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        # قم بإزالة الربط مع hide_hint
        self.entry.bind("<FocusOut>", self.show_hint)

        self.button_configs = [
            ("Reboot", self.reboot_device),
            ("Show Accounts", self.show_account_info),
            ("Download APK", self.browse_file),
            ("Serial", self.show_serial),
            ("Show APK", self.show_installed_apps),
            ("Open App", self.open_app),
            ("Uninstall App", self.uninstall_app),
            ("Download Mode", self.enter_download_mode),
            ("Recovery Mode", self.enter_recovery_mode),
            ("Unlock", self.unlock_screen),
            ("Updates", self.check_for_updates),
            ("Screen Video", self.capture_screen_video),
            ("Developer", self.open_tiktok),
            ("FRP - Android 11", self.bypass_frp),
            ("FRP", self.bypass_with_app),
            ("remove_lock", self.remove_lock),
            ("Enable ADB", lambda: self.enable_adb("COM3"))
        ]

        for index, (text, command) in enumerate(self.button_configs):
            row = (index // 2) + 2
            column = index % 2
            btn = tk.Button(self.bottom_frame2, text=text,bg="#333333", fg="#FFFFFF", command=command, width=15)
            btn.grid(row=row, column=column, padx=5, pady=(5, 10))

    def clear_text(self):
        self.text.delete('1.0', tk.END)
    def show_hint(self, event):
        if not self.entry.get():
            self.hint_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

    def handle_samsung(self):
        self.clear_text()
        self.bottom_frame3.pack_forget()
        self.bottom_frame4.pack_forget()
        self.bottom_frame2.pack(fill=tk.BOTH, expand=True)

    def handle_oppo(self):
        self.clear_text()
        self.bottom_frame2.pack_forget()
        self.bottom_frame4.pack_forget()
        self.bottom_frame3.pack(fill=tk.BOTH, expand=True)

        self.hint_label_oppo = tk.Label(self.bottom_frame3, text="ادخل اسم تطبيق:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.hint_label_oppo.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        self.entry_oppo = tk.Entry(self.bottom_frame3,bg="#444444", fg="#FFFFFF")
        self.entry_oppo.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        self.entry_oppo.bind("<FocusOut>", self.show_hint)

        self.button_configs_oppo = [
            ("Reboot", self.reboot_device),
            ("Data", self.show_account_infoo),
            ("Download APK", self.browse_file),
            ("Serial", self.show_serial),
            ("Show APK", self.show_installed_apps),
            ("Open App", self.open_app),
            ("Uninstall App", self.uninstall_app),
            ("Download Mode", self.enter_download_mode),
            ("Recovery Mode", self.enter_recovery_mode),
            ("Unlock", self.unlock_screen),
            ("Updates", self.check_for_updates),
            ("Screen Video", self.capture_screen_video),
            ("Developer", self.open_tiktok)
        ]

        for index, (text, command) in enumerate(self.button_configs_oppo):
            row = (index // 2) + 2
            column = index % 2
            btn = tk.Button(self.bottom_frame3, text=text,bg="#333333", fg="#FFFFFF" ,command=command, width=15)
            btn.grid(row=row, column=column, padx=5, pady=(5, 10))
            
    def run_command(self, command):
        self.clear_text()  # مسح المخرجات السابقة
        try:
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode() + result.stderr.decode()  # دمج المخرجات
            self.text.insert(tk.END, output)  # عرض النتائج في منطقة النص
        except Exception as e:
            self.text.insert(tk.END, f"حدث خطأ: {e}")  # عرض رسالة الخطأ

    def handle_MTK(self):
        self.clear_text()  # مسح أي مخرجات سابقة
        self.bottom_frame2.pack_forget()  # إخفاء الإطارات الأخرى
        self.bottom_frame3.pack_forget()
        self.bottom_frame4.pack(fill=tk.BOTH, expand=True)  # عرض إطار MTK

        # تسمية لحقل إدخال اسم التطبيق
        self.hint_label_oppo = tk.Label(
            self.bottom_frame4, text="ادخل اسم تطبيق:", bg="#000000", fg="#FFFFFF", font=("Arial", 12)
        )
        self.hint_label_oppo.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        # حقل إدخال اسم التطبيق
        self.entry_oppo = tk.Entry(self.bottom_frame4, bg="#444444", fg="#FFFFFF")
        self.entry_oppo.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        self.entry_oppo.bind("<FocusOut>", self.show_hint)

        # تكوين الأزرار لعمليات MTK
        self.button_configs_MTK = [
            ("Bypass Secure Boot", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py payload")),
            ("Format", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py e userdata")),
            ("Remove FRP", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py e frp")),
            ("Bypass Mi Account", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py e persistent")),
            ("Remove Demo", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py e backup")),
            ("Unlock Bootloader", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py xflash seccfg unlock")),
            ("Relock Bootloader", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py xflash seccfg lock")),
            ("Read Flash", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py rf")),
            ("Write Flash", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py wf")),
            ("Erase Partition", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py e partition_name")),
            ("Get Target Config", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py gettargetconfig")),
            ("Dump BROM", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py dumpbrom")),
            ("Dump SRAM", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py dumpsram")),
            ("Erase Userdata", lambda: self.confirm_action("مسح بيانات المستخدم", "python android_LY-main/mtkclient-main/mtk.py e userdata")),
            ("Read GPT", lambda: self.run_command("python android_LY-main/mtkclient-main/mtk.py printgpt")),
        ]

        # إنشاء الأزرار لكل عملية
        for index, (text, command) in enumerate(self.button_configs_MTK):
            row = (index // 2) + 2
            column = index % 2
            btn = tk.Button(self.bottom_frame4, text=text, bg="#333333", fg="#FFFFFF", command=command, width=15)
            btn.grid(row=row, column=column, padx=5, pady=(5, 10))
                
    def exit_program(self, event=None):
        self.stop_device_check()  # إيقاف التحقق من الجهاز
        self.root.quit()  # إغلاق البرنامج

    def enable_adb(self, cur_com):
        send_log(f"Using port {cur_com}", color="green")
        messagebox.showinfo("Info", "Go to emergency dialer enter *#*#, click OK when done")
        send_log("Initial...", color=None)

        text = at_send_single(cur_com, "AT+KSTRINGB=0,3")
        if "\nOK" in text:
            send_log("OK", color="green")
        else:
            send_log("FAIL", color="red")

        send_log("Method 1", color=None)
        send_log("Step 1...", color=None)

        text = at_send_single(cur_com, "AT+DUMPCTRL=1,0")
        if "\nOK" in text:
            send_log("OK", color="green")
        else:
            send_log("FAIL", color="red")

        send_log("Step 2...", color=None)

        text = at_send_single(cur_com, "AT+DEBUGLVC=0,5")
        if "\nOK" in text:
            send_log("OK", color="green")
        else:
            send_log("FAIL", color="red")

    def check_for_updates(self):
        try:
            response = requests.get("https://api.github.com/repos/bubaker0/android_LY/releases/latest")
            response.raise_for_status()
            latest_version = response.json()["tag_name"]

            if latest_version != self.version:
                # تأكيد من المستخدم
                if messagebox.askyesno("تحديث متاح", f"هل تريد تحديث إلى الإصدار {latest_version}?"):
                    # تحديد اسم الملف تلقائيًا
                    default_filename = f"android_LY_{latest_version}.zip"
                    download_path = filedialog.asksaveasfilename(defaultextension=".zip", initialfile=default_filename, title="حدد مكان تنزيل التحديث", filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")])
                    if download_path:
                        url = response.json()["zipball_url"]
                        r = requests.get(url)
                        r.raise_for_status()
                        with open(download_path, "wb") as f:
                            f.write(r.content)
                        messagebox.showinfo("نجاح", "تم تنزيل التحديث بنجاح!")
            else:
                messagebox.showinfo("لا توجد تحديثات", "أنت تستخدم أحدث إصدار.")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ: {str(e)}")

    def reboot_device(self):
        self.clear_text()
        subprocess.run(["adb", "reboot"])
        
    def show_hint_oppo(self, event):
        if not self.entry_oppo.get():
            self.hint_label_oppo.grid(row=0, column=0, columnspan=2, pady=(10, 5))

    def enter_download_mode(self):
        self.clear_text()
        subprocess.run(["adb", "reboot", "download"])

    def enter_recovery_mode(self):
        self.clear_text()
        subprocess.run(["adb", "reboot", "recovery"])

    def bypass_frp(self):
        self.clear_text()
        os.system("adb start-server")
        os.system("adb shell am broadcast -a android.intent.action.MAIN -n com.android.settings/.Settings")

    def show_account_infoo(self):
        self.clear_text()
        command = ['adb', 'shell', 'dumpsys', 'account']
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
        if result.returncode == 0:
            output = result.stdout.decode('utf-8')
            formatted_output = self.format_account_details(output)
    
            # التحقق مما إذا كانت هناك حسابات Google
            if "Google" not in output:
                google_command = [
                    'adb', 'shell', 'content', 'query',
                    '--uri', 'content://com.google.android.gsf.account',
                    '--projection', 'account_name'
                ]
                google_result = subprocess.run(google_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
                if google_result.returncode == 0:
                    google_output = google_result.stdout.decode('utf-8')
                    formatted_output += "\n\nتفاصيل حسابات Google:\n"
                    formatted_output += google_output  # عرض الناتج مباشرة
                else:
                    formatted_output += "\nلم يتم العثور على حسابات Google أيضًا."
            else:
                formatted_output += "\nتوجد حسابات Google."
    
        else:
            formatted_output = 'حدث خطأ أثناء استرجاع الحسابات'
    
        self.text.insert('1.0', formatted_output)
        
    def show_account_info(self):
        self.clear_text()
        command = ['adb', 'shell', 'dumpsys', 'account']
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            output = result.stdout.decode('utf-8')
            # تنسيق البيانات لعرض تفاصيل الحسابات
            formatted_output = self.format_account_details(output)

            # تحقق مما إذا كانت هناك حسابات
            if "Google" not in output:
                google_command = ['adb', 'shell', 'dumpsys', 'google']
                google_result = subprocess.run(google_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                if google_result.returncode == 0:
                    google_output = google_result.stdout.decode('utf-8')
                    formatted_output += "\n\nتفاصيل حسابات Google:\n"
                    formatted_output += self.format_account_details(google_output)
                else:
                    formatted_output += "\nلم يتم العثور على حسابات Google أيضًا."
        else:
            formatted_output = 'حدث خطأ أثناء استرجاع الحسابات'

        self.text.insert('1.0', formatted_output)

    def format_account_details(self, output):
        # استخراج تفاصيل الحسابات فقط
        lines = output.splitlines()
        account_details = []

        for line in lines:
            if 'Account {' in line:
                account_details.append(line.strip())

        return "\n".join(account_details) if account_details else "لا توجد حسابات."

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("APK Files", "*.apk")])
        if file_path:
            self.clear_text()
            self.text.insert(tk.END, f"تثبيت التطبيق من: {file_path}\n")

            result = subprocess.run(["adb", "install", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8') + '\n' + result.stderr.decode('utf-8')

            self.text.insert(tk.END, output + '\n')

            if "Success" in output:
                self.text.insert(tk.END, "تم تثبيت التطبيق بنجاح.\n")
            else:
                self.text.insert(tk.END, "فشل في تثبيت التطبيق.\n")

    def bypass_with_app(self):
        self.clear_text()

        try:
            # تحديد نوع الجهاز
            device_info = subprocess.check_output("adb shell getprop ro.product.manufacturer", shell=True).decode().strip()

            if device_info.lower() == "samsung":
                # أوامر ADB لأجهزة Samsung
                os.system("adb shell am start -n com.google.android.gsf.login/")
                os.system("adb shell am start -n com.google.android.gsf.login.LoginActivity")
                os.system("adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
            else:
                # أوامر ADB لأجهزة أخرى
                os.system("adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")

            messagebox.showinfo("نجاح", "تم تجاوز FRP بنجاح.")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ: {e}")

    def show_serial(self):
        self.clear_text()
        self.text.delete('1.0', tk.END)

        # الحصول على رقم التسلسلي
        adb_devices = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        serial_number = adb_devices.split('\n')[1].split('\t')[0]

        # الحصول على المعلومات الأخرى
        model = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.model'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        brand = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.brand'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        device_name = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.device'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        product_name = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.name'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        cpu = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.cpu.abi'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        platform = subprocess.run(['adb', 'shell', 'getprop', 'ro.board.platform'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

        # معلومات البرمجيات
        build = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.display.id'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        version = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.version.incremental'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        build_date = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.date'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        fingerprint = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.fingerprint'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        security_patch = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.version.security_patch'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        android_version = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.version.release'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        android_sdk = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.version.sdk'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

        # معلومات الشبكة
        network_type = subprocess.run(['adb', 'shell', 'getprop', 'gsm.network.type'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        sim_operator = subprocess.run(['adb', 'shell', 'getprop', 'gsm.operator.alpha'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        sim_state = subprocess.run(['adb', 'shell', 'getprop', 'gsm.sim.state'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

        # نسبة البطارية
        battery_level = subprocess.run(['adb', 'shell', 'dumpsys', 'battery'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        battery_percentage = ""

        for line in battery_level.splitlines():
            if "level" in line:
                battery_percentage = line.split(":")[1].strip()
                break

        # عرض المعلومات بتنسيق أفضل
        output = (
            f"رقم التسلسلي: {serial_number}\n"
            f"طراز الجهاز: {model}\n"
            f"الماركة: {brand}\n"
            f"اسم الجهاز: {device_name}\n"
            f"اسم المنتج: {product_name}\n"
            f"وحدة المعالجة المركزية: {cpu}\n"
            f"المنصة: {platform}\n\n"
            f"معلومات البرمجيات:\n"
            f"  - البناء: {build}\n"
            f"  - الإصدار: {version}\n"
            f"  - تاريخ البناء: {build_date}\n"
            f"  - البصمة: {fingerprint}\n"
            f"  - تصحيح الأمان: {security_patch}\n"
            f"  - إصدار Android: {android_version}\n"
            f"  - SDK Android: {android_sdk}\n\n"
            f"معلومات الشبكة:\n"
            f"  - نوع الشبكة: {network_type}\n"
            f"  - مشغل SIM: {sim_operator}\n"
            f"  - حالة SIM: {sim_state}\n"
            f"  - نسبة البطارية: {battery_percentage}%\n"
        )

        self.text.insert('1.0', output)
    def show_installed_apps(self):
        self.clear_text()
        self.text.delete('1.0', tk.END)
        packages = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()
        installed_apps = [pkg.split(':')[1] for pkg in packages if pkg]
        self.text.insert(tk.END, "التطبيقات المثبتة:\n" + "\n".join(installed_apps))

    def uninstall_app(self):
        self.clear_text()
        app_name = self.entry.get().strip().lower()

        if not re.match("^[a-zA-Z0-9_.]+$", app_name):
            self.text.insert(tk.END, "يرجى إدخال اسم تطبيق صحيح يتكون من أحرف وأرقام فقط.\n")
            return

        packages = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        app_name = re.sub(r'[^a-zA-Z0-9_.]', '', app_name)

        package_name = next((line.split(':')[1] for line in packages.splitlines() if app_name in line.lower()), None)

        if package_name:
            confirm = messagebox.askyesno("تأكيد", f"هل تريد إلغاء تثبيت {package_name.strip()}؟")
            if confirm:
                try:
                    result = subprocess.run(["adb", "uninstall", package_name.strip()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.text.insert(tk.END, result.stdout.decode('utf-8') + '\n')
                    self.text.insert(tk.END, result.stderr.decode('utf-8') + '\n')
                    messagebox.showinfo("نجاح", "تم إلغاء تثبيت التطبيق بنجاح.")
                except Exception as e:
                    self.text.insert(tk.END, f"حدث خطأ أثناء إلغاء التثبيت: {str(e)}\n")
        else:
            self.text.insert(tk.END, "لم يتم العثور على التطبيق.\n")

    def open_app(self):
        self.clear_text()
        app_name = self.entry.get().strip().lower()

        if not re.match("^[a-zA-Z0-9_.]+$", app_name):
            self.text.insert(tk.END, "يرجى إدخال اسم تطبيق صحيح يتكون من أحرف وأرقام فقط.\n\n")
            return

        packages = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        app_name = re.sub(r'[^a-zA-Z0-9_.]', '', app_name)

        package_name = next((line.split(':')[1] for line in packages.splitlines() if app_name in line.lower()), None)

        if package_name:
            self.text.insert(tk.END, f"جارٍ فتح التطبيق: {package_name.strip()}...\n")
            self.root.update()  # تحديث الواجهة لعرض الرسالة

            try:
                result = subprocess.run(
                    ["adb", "shell", "monkey", "-p", package_name.strip(), "-c", "android.intent.category.LAUNCHER", "1"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                output = result.stdout.decode('utf-8').strip()
                error = result.stderr.decode('utf-8').strip()

                self.clear_text()  # مسح النص قبل عرض النتائج
                if output:
                    self.text.insert(tk.END, f"المخرجات:\n{output}\n\n")
                if error:
                    self.text.insert(tk.END, f"الأخطاء:\n{error}\n\n")

                if "Success" in output:
                    self.text.insert(tk.END, "تم فتح التطبيق بنجاح.\n")
                else:
                    self.text.insert(tk.END, "فشل في فتح التطبيق.\n")
            except Exception as e:
                self.text.insert(tk.END, f"حدث خطأ أثناء فتح التطبيق: {str(e)}\n")
        else:
            self.text.insert(tk.END, "لم يتم العثور على التطبيق. يرجى إدخال اسم تطبيق صحيح.\n")
    
    def unlock_screen(self):
        self.clear_text()
        subprocess.run(["adb", "shell", "cmd", "lock_settings", "clear", "--old", "1234", "--user", "0"])

    def capture_screen_video(self):
        self.clear_text()
        scrcpy_path = os.path.join(os.path.dirname(__file__), "scrcpy-win64-v2.6.1", "scrcpy.exe")

        def run_scrcpy():
            process = subprocess.Popen([scrcpy_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in process.stdout:
                if line.strip():  # تجنب إدراج الأسطر الفارغة
                    formatted_line = f"[INFO] {line.strip()}\n"  # إضافة علامة
                    self.text.insert(tk.END, formatted_line)
                    self.text.see(tk.END)  # Scroll to the end

            for line in process.stderr:
                if line.strip():  # تجنب إدراج الأسطر الفارغة
                    formatted_line = f"[ERROR] {line.strip()}\n"  # إضافة علامة
                    self.text.insert(tk.END, formatted_line)
                    self.text.see(tk.END)

        video_thread = threading.Thread(target=run_scrcpy)
        video_thread.start()
    def open_tiktok(self):
        url = "https://www.tiktok.com/@x_23ly"
        webbrowser.open(url)

def send_log(message, color=None):
    print(message)  # Replace with actual logging mechanism

def at_send_single(cur_com, command):
    return "\nOK"  # Simulate a successful command execution

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
