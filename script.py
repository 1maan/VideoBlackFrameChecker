import cv2
import numpy as np
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import messagebox
import threading

def check_for_full_black(frame, threshold=10):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if np.all(gray < threshold):
        return True
    return False

def process_video(video_path, output_text, progress_label):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open video.")
        return
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = 0
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Processing video: {video_path}\n")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        progress_label.config(text=f"Processing frame {frame_count}/{total_frames}")
        root.update() 

        if check_for_full_black(frame):
            time_in_seconds = frame_count / fps
            minutes = int(time_in_seconds // 60)
            seconds = int(time_in_seconds % 60)
            output_text.insert(tk.END, f"Full black frame detected at {minutes:02}:{seconds:02}\n")
    
    cap.release()
    progress_label.config(text="Processing completed!")

def on_drop(event, output_text, progress_label):
    video_path = event.data.strip("{}")
    if video_path:
        threading.Thread(target=process_video, args=(video_path, output_text, progress_label), daemon=True).start()

def create_gui():
    global root
    root = TkinterDnD.Tk()
    root.title("Video Black Frame Checker By Imaan  v1.0.1")
    root.geometry("600x400")
    root.resizable(False, False)
    root.iconbitmap("icon.ico")

    try:
        label_font = ("Poppins", 14)
    except:
        label_font = ("Helvetica", 14)
    
    progress_font = ("Poppins", 10) if label_font == ("Poppins", 14) else ("Helvetica", 10)
    
    label = tk.Label(root, text="Drag and drop a video file here", font=label_font)
    label.pack(pady=20)
    
    output_text = tk.Text(root, width=70, height=15, font=("Poppins", 10) if label_font == ("Poppins", 14) else ("Helvetica", 10))
    output_text.pack(pady=10)

    progress_label = tk.Label(root, text="Progress: Waiting for file...", font=progress_font)
    progress_label.pack(pady=10)

    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', lambda event: on_drop(event, output_text, progress_label))

    root.mainloop()

if __name__ == "__main__":
    create_gui()
