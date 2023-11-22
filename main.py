import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.filename = "final_file.mp4"
        self.master = master
        self.pack()
        self.create_widgets()

    def marge_videos(self): 
        print(self.filename)
        command = ["bin/ffmpeg", "-f", "concat", "-i", "bin/files.txt", "-vcodec", "copy", "-acodec", "copy", self.filename]

        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print(result.stdout.decode())
        except subprocess.CalledProcessError as e:
            print(f"Error: {str(e)}")

    def create_widgets(self):
        self.select_button = tk.Button(self)
        self.select_button["text"] = "Add MP4 files"
        self.select_button["command"] = self.select_files
        self.select_button.pack(side="top", fill="both", expand=True)

        self.file_listbox = tk.Listbox(self)
        self.file_listbox.pack(side="top", fill="both", expand=True)

        self.output_label = tk.Label(self, text="Destination path:")
        self.output_label.pack(side="top")
        self.output_entry = tk.Entry(self)
        self.output_entry.pack(side="top", fill="both", expand=True)

        self.output_button = tk.Button(self)
        self.output_button["text"] = "Add destination file"
        self.output_button["command"] = self.select_output
        self.output_button.pack(side="top", fill="both", expand=True)

        self.save_button = tk.Button(self)
        self.save_button["text"] = "Start processing"
        self.save_button["command"] = self.save_to_file
        self.save_button.pack(side="top", fill="both", expand=True)

    def select_files(self):
        filenames = filedialog.askopenfilenames(filetypes=[('MP4 files', '*.mp4')])
        filenames = sorted(filenames, key=os.path.getctime)
        self.file_listbox.delete(0, tk.END)
        for filename in filenames:
            self.file_listbox.insert(tk.END, os.path.basename(filename))

    def select_output(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".mp4")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.filename)

    def save_to_file(self):
        output_file = self.output_entry.get()
        if not output_file:
            messagebox.showerror("Error", "Please enter the path to the resulting file.")
            return
        filenames = self.file_listbox.get(0, tk.END)
        with open('./bin/files.txt', 'w') as f:
            for filename in filenames:
                f.write(f"file {os.path.relpath(filename)}\n")
        self.marge_videos()
        messagebox.showinfo("Success", "The files have been merged.")

root = tk.Tk()
root.wm_title("QMV Maker v1.0")
root.wm_iconbitmap('bin/icomax.ico')
#root.geometry("500x500")  # Ustawienie rozmiaru okna na 500x500 pikseli
app = Application(master=root)
app.mainloop()