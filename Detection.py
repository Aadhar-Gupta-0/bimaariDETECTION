"""Simple Tkinter symptom education demo. No diagnostic claims or personal data storage."""
import tkinter as tk
from tkinter import ttk, messagebox
from guidance import SYMPTOMS, evaluate_symptoms


class DetectionApp:
    def __init__(self, patient_name="Guest", patient_age=None):
        self.window = tk.Tk()
        self.window.title("bimaariDETECTION · Symptom Education")
        self.window.minsize(560, 510)
        self.window.geometry("690x650")
        self.window.configure(bg="#f5f7fb")
        self.symptoms = {name: tk.BooleanVar(value=False) for name in SYMPTOMS}
        self._build_ui(patient_name)
        self.window.mainloop()

    def _build_ui(self, patient_name):
        wrap = ttk.Frame(self.window, padding=25)
        wrap.pack(fill="both", expand=True)
        ttk.Label(
            wrap, text="bimaariDETECTION",
            font=("Arial", 24, "bold")
        ).pack(anchor="w")
        ttk.Label(
            wrap, text=f"Welcome, {patient_name}. Learn what to discuss with a clinician.",
            wraplength=560,
        ).pack(anchor="w", pady=(6, 18))
        ttk.Label(
            wrap, text="Select the symptoms you want to learn about:",
            font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=(0, 7))
        for symptom, value in self.symptoms.items():
            ttk.Checkbutton(wrap, text=symptom, variable=value).pack(anchor="w", pady=2)
        controls = ttk.Frame(wrap)
        controls.pack(fill="x", pady=16)
        ttk.Button(controls, text="Explore symptoms", command=self.display_guidance).pack(side="left", padx=(0, 10))
        ttk.Button(controls, text="Reset", command=self.clear).pack(side="left")
        ttk.Label(
            wrap,
            text="Important: Educational software only. This tool does NOT detect disease, "
                 "assess medical risk accurately, replace medical care, or recommend specific doctors.",
            wraplength=585, foreground="#a12332"
        ).pack(anchor="w", pady=(5, 15))
        output_frame = ttk.Frame(wrap)
        output_frame.pack(fill="both", expand=True)
        ttk.Label(output_frame, text="Educational guidance", font=("Arial", 13, "bold")).pack(anchor="w")
        self.output = tk.Text(
            output_frame, height=10, wrap="word",
            font=("Arial", 11), relief="flat", padx=12, pady=12,
            bg="white", fg="#26344c", state="disabled"
        )
        self.output.pack(fill="both", expand=True, pady=(8, 0))
        self.set_output("Choose symptoms and click Explore symptoms. Nothing you enter is saved or transmitted.")

    def set_output(self, message):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", message)
        self.output.configure(state="disabled")

    def display_guidance(self):
        selected = [name for name, value in self.symptoms.items() if value.get()]
        result = evaluate_symptoms(selected)
        lines = [result["headline"], ""]
        lines.extend("• " + item for item in result["guidance"])
        lines.extend([
            "",
            "This app cannot identify the cause of symptoms.",
            "Consult a qualified healthcare professional for proper evaluation.",
        ])
        self.set_output("\n".join(lines))
        if result["level"] == "emergency":
            messagebox.showwarning("Urgent medical attention", result["headline"])

    def clear(self):
        for value in self.symptoms.values():
            value.set(False)
        self.set_output("Select symptoms to view general educational guidance.")


if __name__ == "__main__":
    DetectionApp()
