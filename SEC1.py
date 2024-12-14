import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video(resolution):
    link = url_entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    try:
        yt = YouTube(link)
        if resolution == "high":
            stream = yt.streams.get_highest_resolution()
        elif resolution == "low":
            stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        elif resolution == "audio":
            stream = yt.streams.filter(only_audio=True).first()

        if stream:
            stream.download()
            messagebox.showinfo("Success", f"Download completed: {stream.default_filename}")
        else:
            messagebox.showerror("Error", "No suitable stream found.")
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


