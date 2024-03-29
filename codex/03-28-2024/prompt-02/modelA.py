import tkinter as tk
import tkinter.messagebox as mb
import json

def add_note():
    note = text_area.get("1.0", "end-1c")  # Get the note text
    if note.strip():  # Check if it's not empty
        notes.append(note)
        update_list()
    else:
        mb.showerror("Error", "Note cannot be empty.")

def delete_note():
    selected_index = listbox.curselection()
    if selected_index:
        result = mb.askquestion("Delete", "Are you sure you want to delete this note?")
        if result == 'yes':
            del notes[selected_index[0]]
            update_list()
    else:
        mb.showerror("Error", "No note selected for deletion.")

def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            global notes
            notes = json.load(f)
            update_list()
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist

def update_list():
    listbox.delete(0, tk.END)
    for note in notes:
        listbox.insert(tk.END, note)

# Main application setup
window = tk.Tk()
window.title("Simple Note-Taking App")

# Text area for notes
text_area = tk.Text(window)
text_area.pack(expand=True, fill="both")

# Listbox for displaying notes
listbox = tk.Listbox(window)
listbox.pack(expand=True, fill="both")

# Buttons
frame = tk.Frame(window)
frame.pack()
add_button = tk.Button(frame, text="Add Note", command=add_note)
add_button.pack(side="left")
delete_button = tk.Button(frame, text="Delete Note", command=delete_note)
delete_button.pack(side="left")
save_button = tk.Button(frame, text="Save Notes", command=save_notes)
save_button.pack(side="left")

# Load existing notes
notes = []  # Initialize list to store notes
load_notes()

window.mainloop()