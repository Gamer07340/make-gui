#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess
import os

def select_makefile():
    file_path = filedialog.askopenfilename(title="Select a Makefile", filetypes=[("Makefile", "Makefile")])
    if file_path:
        makefile_path.set(file_path)

def run_make_with_args():
    extra_args = extra_args_entry.get()
    output_text.delete(1.0, tk.END)
    try:
        command = ["make"] + extra_args.split()
        result = subprocess.run(command, cwd=os.path.dirname(makefile_path.get()), capture_output=True, text=True)
        output_text.insert(tk.END, result.stdout + result.stderr)
    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}\n")

root = tk.Tk()
root.title("Make Interface")

# Ajout de l'icône
icon = tk.PhotoImage(file="make-gui.png")
root.tk.call("wm", "iconphoto", root._w, icon)

makefile_path = tk.StringVar()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Select Makefile", command=select_makefile).pack()
tk.Label(frame, textvariable=makefile_path).pack()

tk.Label(root, text="Additional arguments:").pack()
extra_args_entry = tk.Entry(root, width=50)
extra_args_entry.pack(pady=5)

tk.Button(root, text="Make!", command=run_make_with_args).pack()

output_text = scrolledtext.ScrolledText(root, height=10, width=50)
output_text.pack(pady=5)

root.mainloop()

