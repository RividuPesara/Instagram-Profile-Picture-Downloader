import instaloader
import tkinter as tk
from tkinter import messagebox

def download_picture(event=None):
    username = entryName.get()

    loader = instaloader.Instaloader()

    try:
        loader.download_profile(username, profile_pic_only=True)
        messagebox.showinfo("Success", f"Profile picture of {username} downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download profile picture")

root = tk.Tk()
root.title("Instagram Profile Picture Downloader")
root.geometry("450x100")

labelName = tk.Label(root, text="Enter the username:")
labelName.pack(pady=2)
entryName = tk.Entry(root, width=30)
entryName.bind('<Return>', download_picture)
entryName.pack(pady=2)

downloadButton = tk.Button(root, text="Download", command=download_picture)
downloadButton.pack(pady=2)

root.mainloop()
