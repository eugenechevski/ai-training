import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class Notepad:
    def __init__(self, root):
        self.root = root
        self.text = tk.Text(self.root)
        self.text.pack()

        # Create a menu bar
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

    def new_file(self):
        self.text.delete(1.0, tk.END)

    def open_file(self):
        file = filedialog.askopenfile(
            mode='r', filetypes=[('Text Files', '*.txt')])
        if file is not None:
            content = file.read()
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.INSERT, content)

    def save_file(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[
                                        ('Text Files', '*.txt')])
        if file is not None:
            data = self.text.get(1.0, tk.END)
            file.write(data)
            file.close()


root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
