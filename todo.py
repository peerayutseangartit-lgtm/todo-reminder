import tkinter as tk
from tkinter import messagebox
import threading
import time

class TodoReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List & Reminder")
        self.root.geometry("400x500")

        # ส่วนหัวข้อ
        self.label = tk.Label(root, text="รายการสิ่งที่ต้องทำ", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # ช่องกรอกงาน
        self.task_entry = tk.Entry(root, width=35, font=("Helvetica", 12))
        self.task_entry.pack(pady=5)
        self.task_entry.insert(0, "กรอกงานที่นี่...")

        # ช่องกรอกเวลา (นาที)
        self.time_label = tk.Label(root, text="ตั้งเวลาแจ้งเตือน (นาที):", font=("Helvetica", 10))
        self.time_label.pack()
        self.time_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
        self.time_entry.pack(pady=5)
        self.time_entry.insert(0, "1")

        # ปุ่มเพิ่มงาน
        self.add_button = tk.Button(root, text="เพิ่มงานและตั้งเวลา", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=10)

        # รายการ Listbox
        self.tasks_listbox = tk.Listbox(root, width=45, height=10, font=("Helvetica", 12))
        self.tasks_listbox.pack(pady=10)

        # ปุ่มลบงาน
        self.delete_button = tk.Button(root, text="ลบงานที่เลือก", command=self.delete_task, bg="#f44336", fg="white")
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        timer_val = self.time_entry.get()

        if task != "" and task != "กรอกงานที่นี่...":
            try:
                # แปลงเวลาเป็นวินาที
                seconds = int(timer_val) * 60
                self.tasks_listbox.insert(tk.END, f"{task} (อีก {timer_val} นาที)")
                
                # เริ่ม Thread สำหรับการแจ้งเตือน (เพื่อไม่ให้ GUI ค้าง)
                threading.Thread(target=self.set_reminder, args=(task, seconds), daemon=True).as_start()
                
                self.task_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("ข้อผิดพลาด", "กรุณากรอกเวลาเป็นตัวเลขจำนวนเต็ม")
        else:
            messagebox.showwarning("คำเตือน", "กรุณากรอกชื่องาน")

    def set_reminder(self, task, seconds):
        # รอเวลาตามที่กำหนด
        time.sleep(seconds)
        # แสดงหน้าต่างแจ้งเตือน
        messagebox.showinfo("Reminder", f"ถึงเวลาทำ: {task} แล้ว!")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("คำเตือน", "กรุณาเลือกงานที่ต้องการลบ")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoReminderApp(root)
    root.mainloop()