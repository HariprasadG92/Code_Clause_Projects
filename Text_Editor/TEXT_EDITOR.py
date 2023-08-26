import tkinter as tk
from tkinter import filedialog, messagebox, font
from tkinter import ttk  

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        
        self.style_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Style", menu=self.style_menu)
        
        self.font_menu = tk.Menu(self.style_menu, tearoff=0)
        self.style_menu.add_cascade(label="Font", menu=self.font_menu)
        
        self.font_size_menu = tk.Menu(self.style_menu, tearoff=0)
        self.style_menu.add_cascade(label="Font Size", menu=self.font_size_menu)
        
        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Word Count", command=self.count_words)
        self.view_menu.add_command(label="Line Count", command=self.count_lines)
        self.view_menu.add_command(label="Toggle Dark Theme", command=self.toggle_dark_theme)  # Add dark theme toggle
        
        self.font_family = tk.StringVar()
        self.font_size = tk.StringVar()
        
        self.font_families = font.families()
        self.font_sizes = list(range(8, 72, 2))
        
        self.font_family.set("Arial")
        self.font_size.set("12")
        
        for family in self.font_families:
            self.font_menu.add_radiobutton(label=family, variable=self.font_family, command=self.change_font_family)
            
        for size in self.font_sizes:
            self.font_size_menu.add_radiobutton(label=str(size), variable=self.font_size, command=self.change_font_size)
        
        self.current_file = None
        self.current_font = (self.font_family.get(), int(self.font_size.get()))
        self.dark_theme = False  
        
        self.text_area.config(font=self.current_font)
        
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.current_file = file_path
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
        
    def save_file(self):
        if self.current_file:
            content = self.text_area.get(1.0, tk.END)
            with open(self.current_file, "w") as file:
                file.write(content)
        else:
            self.save_file_as()
        
    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.current_file = file_path
            self.save_file()

    def change_font_family(self):
        self.current_font = (self.font_family.get(), int(self.font_size.get()))
        self.text_area.config(font=self.current_font)

    def change_font_size(self):
        self.current_font = (self.font_family.get(), int(self.font_size.get()))
        self.text_area.config(font=self.current_font)
        
    def count_words(self):
        content = self.text_area.get(1.0, tk.END)
        words = content.split()
        num_words = len(words)
        messagebox.showinfo("Word Count", f"Total words: {num_words}")
        
    def count_lines(self):
        content = self.text_area.get(1.0, tk.END)
        lines = content.split("\n")
        num_lines = len(lines)
        messagebox.showinfo("Line Count", f"Total lines: {num_lines}")
    
    def toggle_dark_theme(self):
        if self.dark_theme:
            self.text_area.config(bg="white", fg="black") 
        else:
            self.text_area.config(bg="black", fg="white")  
        
        self.dark_theme = not self.dark_theme  

if __name__ == "__main__":
    root = tk.Tk()
    editor = SimpleTextEditor(root)
    root.mainloop()
