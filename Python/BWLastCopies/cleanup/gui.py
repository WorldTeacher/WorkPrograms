from tkinter import filedialog as fd
import tkinter as tk

#* In case I would like to create a GUI for this
class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("BWLastCopies")
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.master.configure(background="white")
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.bind("<Alt-F4>", self.on_closing)
        self.master.filename = None
        

    
    def on_closing(self, event=None):
        self.master.destroy()
        self.master.quit()
        exit()
    def start_run(self):
        self.show_file_contents()
        self.display_message("Start run")
        #add code to start run

        
        exit()
    def file_dialog(self):
        self.master.filename = fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("xml files","*.xml"),("all files","*.*")))
    def display_message(self, message):
        tk.Label(self.master, text=message).grid(row=1, column=0, columnspan=3)
    def show_file_contents(self):
        if self.master.filename:
            with open(self.master.filename, "r") as f:
                self.display_message(f.read())
        else:
            self.display_message("No file selected")
        
    
    def mainloop(self):
        #add a button
        self.create_button("Exit", self.on_closing, 0, 0)
        self.create_button("Start", self.start_run, 0, 1)
        #create a button that opens a file dialog
        self.create_button("Open", self.file_dialog, 0, 2)
        self.display_message("Hello World!")
        
        self.master.mainloop()
        
    #create a button
    def create_button(self, text, command, row, column, rowspan=1, columnspan=1, sticky="NSEW"):
        button = tk.Button(self.master, text=text, command=command)
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky=sticky)
        return button
if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    gui.mainloop()
    exit()