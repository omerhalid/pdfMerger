import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs(paths, output):
    merger = PdfMerger()

    for pdf in paths:
        merger.append(pdf)

    merger.write(output)
    merger.close()

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[('PDF Files', '*.pdf')])

    if not file_paths:
        return

    output_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')

    if not output_file_path:
        return

    try:
        merge_pdfs(file_paths, output_file_path)
        messagebox.showinfo('Success!', 'PDFs merged successfully!')
    except Exception as e:
        messagebox.showerror('Error', str(e))

if __name__ == '__main__':
    root = tk.Tk()
    root.title('PDF Merger')
    root.geometry('300x200')

    merge_button = tk.Button(root, text='Merge PDFs', command=select_files)
    merge_button.pack(expand=True)

    root.mainloop()
