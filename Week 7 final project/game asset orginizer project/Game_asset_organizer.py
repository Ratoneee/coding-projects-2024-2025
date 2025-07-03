import os
import shutil
import tkinter as tk
from tkinter import filedialog

def get_file_type(filename):
    if filename.endswith(('.fbx', '.dae', '.obj', '.stl')):
        return '3D Models'
    elif filename.endswith(('.py', '.cs')):
        return 'Code'
    elif filename.endswith(('.png', '.jpeg', '.jpg', '.bmp')):
        return 'Textures'
    elif filename.endswith(('.mp3', '.wav', '.ogg')):
        return 'Sounds'
    else:
        return 'Others'

def organize_files(source_directory):
    categories = ['3D Models', 'Code', 'Textures', 'Sounds', 'Others']
    for category in categories:
        category_path = os.path.join(source_directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    for root, _, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_type = get_file_type(file)
            category_folder = os.path.join(source_directory, file_type)
            file_subfolder = os.path.join(category_folder, file.split('.')[0])
            if not os.path.exists(file_subfolder):
                os.makedirs(file_subfolder)
            shutil.move(file_path, os.path.join(file_subfolder, file))

def browse_for_folder(entry_field):
    folder_selected = filedialog.askdirectory(title="Select Folder")
    if folder_selected:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, folder_selected)

def start_organizing(entry_field, window):
    folder_path = entry_field.get()
    if os.path.isdir(folder_path):
        organize_files(folder_path)
        success_label = tk.Label(window, text="Assets have been organized!", fg="white", bg="#2e2e2e", font=("Arial", 14))
        success_label.pack(pady=20)
    else:
        error_label = tk.Label(window, text="Invalid folder path. Please try again.", fg="red", bg="#2e2e2e", font=("Arial", 14))
        error_label.pack(pady=20)

def setup_gui():
    window = tk.Tk()
    window.title("Game Asset Organizer")
    window.geometry("800x300")
    window.resizable(True, True)
    window.configure(bg="#2e2e2e")
    label = tk.Label(window, text="Please paste path or select the folder containing your game assets.", fg="white", bg="#2e2e2e", font=("Arial", 14))
    label.pack(pady=20)
    entry_field = tk.Entry(window, width=40, font=("Arial", 12))
    entry_field.pack(pady=10)
    browse_button = tk.Button(window, text="Browse", command=lambda: browse_for_folder(entry_field), bg="white", fg="black", font=("Arial", 12))
    browse_button.pack(pady=5)
    start_button = tk.Button(window, text="Start Organizing", command=lambda: start_organizing(entry_field, window), bg="white", fg="black", font=("Arial", 12))
    start_button.pack(pady=10)
    window.mainloop()

setup_gui()
