import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video(resolution):
    link = url_entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    try:
        ydl_opts = {}
        if resolution == "high":
            ydl_opts = {"format": "bestvideo+bestaudio/best"}
        elif resolution == "low":
            ydl_opts = {"format": "worstvideo+worstaudio/worst"}
        elif resolution == "audio":
            ydl_opts = {"format": "bestaudio", "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}]}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x200")

url_label = tk.Label(root, text="YouTube Video URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

btn_high = tk.Button(root, text="Download High Quality", command=lambda: download_video("high"))
btn_high.pack(pady=5)

btn_low = tk.Button(root, text="Download Low Quality", command=lambda: download_video("low"))
btn_low.pack(pady=5)

btn_audio = tk.Button(root, text="Download Audio Only", command=lambda: download_video("audio"))
btn_audio.pack(pady=5)

root.mainloop()