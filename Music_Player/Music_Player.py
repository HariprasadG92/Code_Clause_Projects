import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.configure(bg="#202020")  # background color
        
        self.playlist = []
        self.current_track = 0

        self.init_ui()
        pygame.init()
    
    def init_ui(self):
        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="#303030", fg="white")
        self.playlist_box.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.frame = tk.Frame(self.root, bg="#202020")  # background color
        self.frame.pack(padx=20, pady=20)

        button_color = "#444444"  # Dark gray color for buttons
        
        self.play_button = tk.Button(self.frame, text="Play ▶️", command=self.play_music, bg=button_color, fg="white")
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(self.frame, text="Pause ⏹", command=self.pause_music, bg=button_color, fg="white")
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.resume_button = tk.Button(self.frame, text="Resume ⏸", command=self.resume_music, bg=button_color, fg="white")
        self.resume_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.frame, text="Next ➡", command=self.next_track, bg=button_color, fg="white")
        self.next_button.pack(side=tk.LEFT, padx=10)

        self.prev_button = tk.Button(self.frame, text="Previous ⬅", command=self.prev_track, bg=button_color, fg="white")
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self.frame, text="Add", command=self.add_track, bg=button_color, fg="white")
        self.add_button.pack(side=tk.LEFT, padx=10)

    def play_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.current_track])
        pygame.mixer.music.play()

    def prev_track(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.current_track])
        pygame.mixer.music.play()

    def add_track(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.playlist.append(file_path)
            self.playlist_box.insert(tk.END, os.path.basename(file_path))
            print(f"Added: {os.path.basename(file_path)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
