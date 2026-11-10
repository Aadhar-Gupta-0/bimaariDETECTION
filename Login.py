"""Optional local welcome screen. Does not write personally identifying records."""
import tkinter as tk
from tkinter import ttk, messagebox
from Detection import DetectionApp


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("bimaariDETECTION")
        self.root.minsize(450, 350)
        self.root.geometry("540x400")
        self.root.configure(bg="#f5f7fb")
        panel = ttk.Frame(root, padding=35)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="bimaariDETECTION", font=("Arial", 24, "bold")).pack(pady=(0, 12))
        ttk.Label(
            panel, text="A privacy-conscious educational symptom explorer.",
            wraplength=440
        ).pack(pady=(0, 22))
        ttk.Label(panel, text="First name or nickname (optional)").pack(anchor="w")
        self.name = ttk.Entry(panel)
        self.name.pack(fill="x", pady=(4, 18))
        ttk.Label(panel, text="Age (optional)").pack(anchor="w")
        self.age = ttk.Entry(panel)
        self.age.pack(fill="x", pady=(4, 16))
        ttk.Button(panel, text="Continue", command=self.continue_to_explorer).pack(fill="x")
        ttk.Label(
            panel, text="Educational use only. Not a diagnostic or medical advice tool.",
            foreground="#a12332", wraplength=420,
        ).pack(pady=20)

    def continue_to_explorer(self):
        age = self.age.get().strip()
        if age and (not age.isdigit() or not 1 <= int(age) <= 120):
            messagebox.showerror("Invalid age", "Enter a valid age (1–120), or leave the field blank.")
            return
        nickname = self.name.get().strip()[:60] or "Guest"
        self.root.destroy()
        DetectionApp(patient_name=nickname, patient_age=int(age) if age else None)


if __name__ == "__main__":
    root = tk.Tk()
    LoginApp(root)
    root.mainloop()
