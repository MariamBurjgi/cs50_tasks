import tkinter as tk

def count_chars(event):
    text = entry.get()
    char_count.set(len(text))

root = tk.Tk()
root.title("character Counter")

label = tk.Label(root, text="Enter text:")
label.pack()

entry = tk.Entry(root)
entry.bind("<KeyRelease>", count_chars)
entry.pack()

char_count = tk.StringVar()
char_count.set("0")

count_label = tk.Label(root, textvariable=char_count)
count_label.pack()

root.mainloop()
