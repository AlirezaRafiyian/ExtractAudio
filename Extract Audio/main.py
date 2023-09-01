import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedStyle
from moviepy.editor import VideoFileClip

"""Extract audio from videos"""

#Func for gathering files name
def get_file_names(folder_path):
    file_names = []
    # Walk through the directory and gather file names
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(file)
    
    return file_names

#Func for browsing a folder 
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        file_names = get_file_names(folder_path)
        file_listbox.delete(0, tk.END)
        for file_name in file_names:
            file_listbox.insert(tk.END, file_name)
    return folder_path

#Func to extract audios
def extract_audio(video_path, output_path):
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_path)
        # Close the clips to free up resources
        audio_clip.close()
        video_clip.close()
        
#Func to start the extracting process
def action():
     folder_path = browse_folder()
     file_names = get_file_names(folder_path)    
     for name in file_names:
          input_video_path = "Video\{fname}".format(fname= name)
          print(input_video_path)
          output_audio_path = "Audio\{fname}".format(fname= name.replace('.mp4', '.mp3'))
          extract_audio(input_video_path, output_audio_path)
          file_listbox.insert(tk.END, '{aname} extracted sucssfully'.format(aname= output_audio_path.replace("Audio\\", '')))

#Create the main application window
root = tk.Tk()
root.title("File Name Extractor")

#Apply a theme
style = ThemedStyle(root)
style.set_theme("arc")

#Create a frame for the content
content_frame = ttk.Frame(root)
content_frame.pack(padx=100, pady=100, expand=True)

#Button for extracting process 
extract_audios = ttk.Button(content_frame, text='Extract', command=action)
extract_audios.pack(pady=30)

# Create a listbox to display the file names
file_listbox = tk.Listbox(content_frame, height=15, width=50)
file_listbox.pack(fill=tk.BOTH, expand=True)

# Start the GUI event loop
root.mainloop()

