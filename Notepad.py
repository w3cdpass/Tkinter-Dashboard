import tkinter as tk
from tkinter import filedialog

class NotePad:
    def __init__(self,root):
        self.root = root
        self.file_path = False
        root.title("NotePad")
        root.geometry("929x850")
        root.iconbitmap("notepad.ico")
        root.config(bg="#a0c7e1")
        # heading = tk.Label(text="Notepad",font=("harlow solid italic",30),bg="#a7e2e6",padx=35,pady=25)
        # heading.grid(row=1,column=2)

        open_btn = tk.Button(text="Open",font=("arial",12),relief='flat',width=7,bg="#a0c7e1",command=self.file_open)
        save_btn = tk.Button(text="Save",font=("arial",12),relief='flat', width=7,bg="#a0c7e1",command=self.save)
        clear_btn = tk.Button(text="Clear",font=("arial",12),relief='flat', width=7,bg="#a0c7e1",command=self.clear)# current object of class and also it is in __init__(self)
        saveas_btn = tk.Button(text="Save as",font=("arial",12),relief='flat', width=7,bg="#a0c7e1",command=self.saveAS)
        exit_btn = tk.Button(text="Help",font=("arial",12),relief='flat', width=7,bg="#a0c7e1",command=self.exit)

        # text_area
        self.text_area = tk.Text(root, font=('arial', 24), relief='raised', wrap=tk.WORD,width=50, height=20)
        self.text_area.grid(row=2, column=0, columnspan=5, padx=10, pady=10, ipadx=2, ipady=2)

        open_btn.grid(row=1,column=0,padx=0,pady=5)
        save_btn.grid(row=1, column=1,padx=0,pady=5)
        clear_btn.grid(row=1,column=2,padx=0,pady=5)
        saveas_btn.grid(row=1,column=3,padx=0,pady=5)
        exit_btn.grid(row=1,column=4,padx=0,pady=5)
        
        
    def clear(self):
        self.text_area.delete(0.0,tk.END)
    # def save(self):
    #     pass
    def file_open(self):
        self.file_path = filedialog.askopenfilename()
        # print(file_path)
        with open(self.file_path,'r') as my_file:
            file_contents = my_file.read()
            self.clear()
            self.text_area.insert(0.0,file_contents)
        my_file = open(self.file_path, 'r')
        text = my_file.read()
        my_file.close()
        self.clear()
        self.text_area.insert(0.0,text)
        self.root.title(self.file_path)
        
    def save(self):
        if self.file_path:
            text = self.text_area.get(0.0,tk.END)
            with open(self.file_path, "w") as my_file:
                my_file.write(text)
        else:
            self.save()
            
    
    def saveAS(self):
        file_options = [("Textfile","*.txt"),("Batfile","*.bat"),("Pythonfile",".py"), ("Allfiles", "*")]
        path = filedialog.asksaveasfilename(defaultextension='.txt',filetypes=file_options)
        text = self.text_area.get(0.0,tk.END)
        with open(path, 'w') as my_file:
            my_file.write(text)
    def exit(self):
        help_text = '''
        
NOTEPAD SHORTCUT KEYS LIST:
Esc: Close an open dialog box.
F1: Open the Microsoft help option for Notepad.
F5: To insert the current time and date.
Alt + E: Open Edit menu.
Alt + F: Open File menu.
Alt + H: Open Help menu.
Alt + O: Open Format menu.
Alt + V: Open View menu.
Ctrl + Tab: To give space between text.
Ctrl + [- or +]: To zoom in and out the page, press Ctrl and "-" for zoom out and "+"
for zoom in. Ctrl + A: Select all the text or characters on the page.
Ctrl + E: This combination of keys is used to search that letter, word, or special character
on the Bing search engine. [For that first point the text cursor behind that letter, word,
or special character]
Ctrl + F or F3: Open the text Find dialog box.
Ctrl + H: Open the text Replace dialog box.
Ctrl + I: To give space between the text.
Ctrl + J or Ctrl + M: This combination of keys is used to break the line.
Ctrl + N: Open a new note in the same window.
Ctrl + Shift + N: Open a new note in a new window.
Ctrl + P: Open the Print dialog box.
Ctrl + S: To Save the note.
Ctrl + Shift + S: Open the Save dialog box so that you can browse a file location to
save the note. Ctrl + W: Close the Notepad window.
AltGr or F10: Switch the text cursor into the normal select mode.
PgUp: Go to the top of the page
        '''
        self.clear()
        self.text_area.insert(0.0,help_text)

# n = NotePad()
# n.


# myenrty = tk.Entry() 
# myenrty.pack()
window = tk.Tk()
note = NotePad(window)

# main loop
window.mainloop()