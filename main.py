import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as tb
import os
import subprocess
import time
from tkinter import messagebox
import threading
import webbrowser
import requests

class App():
    def __init__(self, root):
        self.root = root
        self.version = "1.0.1"
        self.root.title(f"Android_LY - V{self.version}")

        Ft0 = tb.Frame(root, bootstyle="danger", width=400, height=500)
        Ft1 = tb.Frame(root, bootstyle="info", width=400, height=500)

        self.text = tk.Text(Ft1, wrap='word')
        self.text.pack(side='left', fill='both', expand=True)

        bu11 = tb.Button(Ft0, text="updates", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.check_for_updates)
        bu11.place(x=120, y=130)

        bu1 = tb.Button(Ft0, text="Reboot", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.reboot_device)
        bu1.place(x=10, y=30)

        bu2 = tb.Button(Ft0, text="data", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.Acc1)
        bu2.place(x=10, y=80)

        bu3 = tb.Button(Ft0, text="Downloas_APK", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.browse_file)
        bu3.place(x=10, y=130)

        bu4 = tb.Button(Ft0, text="serial", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.ser)
        bu4.place(x=10, y=180)

        bu5 = tb.Button(Ft0, text="Show apk", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.Show1)
        bu5.place(x=10, y=230)

        bu6 = tb.Button(Ft0, text="Open app", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.open_app)
        bu6.place(x=10, y=280)

        bu7 = tb.Button(Ft0, text="uninstall app", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.uninstall_app)
        bu7.place(x=10, y=330)

        bu8 = tb.Button(Ft0, text="d_mode", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.enter_download_mode)
        bu8.place(x=10, y=380)

        bu9 = tb.Button(Ft0, text="Recovery", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.enter_recovery_mode)
        bu9.place(x=10, y=430)

        bu10 = tb.Button(Ft0, text="unlock", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.unlock_screen)
        bu10.place(x=120, y=30)

        bu11 = tb.Button(Ft0, text="screen_v", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.qwe)
        bu11.place(x=120, y=80)

        bu12 = tb.Button(Ft0, text="developer", style="success.Outline.TButton", bootstyle="success, outline", width=8, command=self.open_tiktok)
        bu12.place(x=120, y=430)

        self.current_process = None

        EN1 = tb.Entry(Ft0, state="info")
        EN1.place(x=220, y=30)

        Ft0.grid(column=1, row=0)
        Ft1.grid(column=0, row=0)

    def check_for_updates(self):
        try:
            response = requests.get("https://api.github.com/repos/bubaker0/android_LY/releases/latest")
            response.raise_for_status()
            latest_version = response.json()["tag_name"]
            if latest_version != self.version:
                download_path = filedialog.asksaveasfilename(
                    defaultextension=".zip",
                    title="حدد مكان تنزيل التحديث",
                    filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")]
                )
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
            messagebox.showerror("خطأ", str(e))

    def reboot_device(self):
        subprocess.run(["adb", "reboot"])

    def enter_download_mode(self):
        subprocess.run(["adb", "reboot", "download"])

    def enter_recovery_mode(self):
        subprocess.run(["adb", "reboot", "recovery"])

    def Acc1(self):
        self.text.delete('1.0', tk.END)
        command = ['adb', 'shell', 'dumpsys', 'account']
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            output = result.stdout.decode('utf-8')
            self.text.insert('1.0', output)
        else:
            self.text.insert('1.0', 'An error occurred recovering accounts')

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        os.system("adb install " + file_path)

    def ser(self):
        self.text.delete('1.0', tk.END)
        adb_devices = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        serial_number = adb_devices.split('\n')[1].split('\t')[0]
        model = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.model'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        self.text.insert('1.0', f"Your device serial number is: {serial_number}\n")
        self.text.insert('end', f"Your device model is: {model}")

    def Show1(self):
        self.text.delete('1.0', tk.END)
        packages = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        external_packages = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages', '-3'], stdout=subprocess.PIPE).stdout.decode('utf-8')

        formatted_list = [pkg.split(':')[1][4:] for pkg in packages.split('\n') if pkg]
        external_list = [pkg.split(':')[1][4:] for pkg in external_packages.split('\n') if pkg]

        social_media_apps = {
            "facebook": "com.facebook.katana",
            "instagram": "com.instagram.android",
            "twitter": "com.twitter.android",
            "snapchat": "com.snapchat.android",
            "tiktok": "com.tiktok.viral",
            "youtube": "com.google.android.youtube",
            "chrome": "com.android.chrome"
        }

        social_apps = sorted([name for name in formatted_list if name in social_media_apps.values()])
        system_apps = sorted([name for name in formatted_list if name not in external_list and name not in social_apps])
        sorted_external_apps = sorted(external_list)

        total_count = len(formatted_list)
        self.text.insert(tk.END, f"عدد التطبيقات المثبتة: {total_count}\n\n")

        if social_apps:
            self.text.insert(tk.END, "تطبيقات تواصل اجتماعي:\n")
            for name in social_apps:
                app_name = name.split('.')[-1]
                self.text.insert(tk.END, f"  - {app_name}\n")
            self.text.insert(tk.END, "\n")

        if system_apps:
            self.text.insert(tk.END, "تطبيقات النظام:\n")
            for name in system_apps:
                app_name = name.split('.')[-1]
                self.text.insert(tk.END, f"  - {app_name}\n")

        if sorted_external_apps:
            self.text.insert(tk.END, "\nتطبيقات مثبتة من مصادر خارجية:\n")
            for name in sorted_external_apps:
                app_name = name.split('.')[-1]
                self.text.insert(tk.END, f"  - {app_name}\n")

        self.text.insert(tk.END, "\n--- نهاية القائمة ---\n")

    def uninstall_app(self):
        package_name = EN1.get()
        subprocess.run(["adb", "uninstall", package_name])

    def open_app(self):
        app_name = EN1.get().strip().lower()
        packages = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        package_name = None
        for line in packages.splitlines():
            if app_name in line.lower():
                package_name = line.split(':')[1]
                break
        if package_name:
            subprocess.run(["adb", "shell", "monkey", "-p", package_name.strip(), "-c", "android.intent.category.LAUNCHER", "1"])
        else:
            messagebox.showwarning("تحذير", "يرجى إدخال اسم تطبيق صحيح.")

    def unlock_screen(self):
        subprocess.run(["adb", "shell", "input", "keyevent", "128"])

    def capture_screen_video(self):
        subprocess.call(["scrcpy"])

    def qwe(self):
        video_thread = threading.Thread(target=self.capture_screen_video)
        video_thread.start()

    def open_tiktok(self):
        url = "https://www.tiktok.com/@x_23ly"
        webbrowser.open(url)

root = tb.Window(themename="superhero")
app = App(root)
root.mainloop()