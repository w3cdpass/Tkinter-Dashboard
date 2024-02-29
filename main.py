import tkinter as tk

def open_joke_app():
    import tkinter as tk
    from tkinter import messagebox
    from function import api_function

    def get_joke():
        try:  
            joke = api_function.call()
            text.config(state=tk.NORMAL)
            text.insert(tk.END, joke + "\n\n")
            text.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_text():
        text.config(state=tk.NORMAL)
        text.delete('1.0', tk.END)
        text.config(state=tk.DISABLED)
        rating_label.config(text="Rating: ")

    def rate_joke(rating):
        text.config(state=tk.NORMAL)
        text.insert(tk.END, f"Thank you for rating: {rating} stars\n\n")
        text.config(state=tk.DISABLED)
        rating_label.config(text=f"Rating: {rating} stars")

    root = tk.Tk()
    root.title("Joke App")
    root.iconbitmap("smile.ico")
    
    label = tk.Label(root, text="Click the button to get a joke!")
    label.pack(pady=10)
    
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)
    
    get_joke_button = tk.Button(button_frame, text="Get Joke", command=get_joke, padx=10, pady=5, bg="lightblue")
    get_joke_button.pack(side=tk.LEFT, padx=5)
    
    clear_button = tk.Button(button_frame, text="Clear", command=clear_text, padx=10, pady=5, bg="lightcoral")
    clear_button.pack(side=tk.LEFT, padx=5)
    
    rate_frame = tk.Frame(root)
    rate_frame.pack(pady=5)
    
    label_rate = tk.Label(rate_frame, text="Rate the joke:")
    label_rate.pack(side=tk.LEFT, padx=5)
    
    for i in range(1, 6):
        rate_button = tk.Button(rate_frame, text=str(i), padx=10, pady=5, command=lambda i=i: rate_joke(i))
        rate_button.pack(side=tk.LEFT)
    
    global text
    text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
    text.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)
    text.config(state=tk.DISABLED)
    
    global rating_label
    rating_label = tk.Label(root, text="Rating: ")
    rating_label.pack(pady=10)
    
    root.mainloop()
    

def open_notepad():
    import tkinter as tk
    from tkinter import filedialog
    
    class NotePad:
        def __init__(self,root):
            self.root = root
            self.file_path = False
            root.title("NotePad")
            root.geometry("929x800")
            root.iconbitmap("notepad.ico")
            root.config(bg="#a0c7e1")

            open_btn = tk.Button(root, text="Open", font=("arial", 12), relief='flat', width=7, bg="#a0c7e1", command=self.file_open)
            save_btn = tk.Button(root, text="Save", font=("arial", 12), relief='flat', width=7, bg="#a0c7e1", command=self.save)
            clear_btn = tk.Button(root, text="Clear", font=("arial", 12), relief='flat', width=7, bg="#a0c7e1", command=self.clear)
            saveas_btn = tk.Button(root, text="Save as", font=("arial", 12), relief='flat', width=7, bg="#a0c7e1", command=self.saveAS)
            exit_btn = tk.Button(root, text="Help", font=("arial", 12), relief='flat', width=7, bg="#a0c7e1", command=self.exit)

            self.text_area = tk.Text(root, font=('arial', 24), relief='raised', wrap=tk.WORD, width=50, height=20)
            self.text_area.grid(row=2, column=0, columnspan=5, padx=10, pady=10, ipadx=2, ipady=2)

            open_btn.grid(row=1, column=0, padx=0, pady=5)
            save_btn.grid(row=1, column=1, padx=0, pady=5)
            clear_btn.grid(row=1, column=2, padx=0, pady=5)
            saveas_btn.grid(row=1, column=3, padx=0, pady=5)
            exit_btn.grid(row=1, column=4, padx=0, pady=5)

        def clear(self):
            self.text_area.delete(0.0, tk.END)

        def file_open(self):
            self.file_path = filedialog.askopenfilename()
            with open(self.file_path, 'r') as my_file:
                file_contents = my_file.read()
                self.clear()
                self.text_area.insert(0.0, file_contents)
            my_file = open(self.file_path, 'r')
            text = my_file.read()
            my_file.close()
            self.clear()
            self.text_area.insert(0.0, text)
            self.root.title(self.file_path)

        def save(self):
            if self.file_path:
                text = self.text_area.get(0.0, tk.END)
                with open(self.file_path, "w") as my_file:
                    my_file.write(text)
            else:
                self.save()

        def saveAS(self):
            file_options = [("Textfile", "*.txt"), ("Batfile", "*.bat"), ("Pythonfile", ".py"), ("Allfiles", "*")]
            path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=file_options)
            text = self.text_area.get(0.0, tk.END)
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
            Ctrl + [- or +]: To zoom in and out the page, press Ctrl and "-" for zoom out and "+" for zoom in. 
            Ctrl + A: Select all the text or characters on the page.
            Ctrl + E: This combination of keys is used to search that letter, word, or special character on the Bing search engine. [For that first point the text cursor behind that letter, word, or special character]
            Ctrl + F or F3: Open the text Find dialog box.
            Ctrl + H: Open the text Replace dialog box.
            Ctrl + I: To give space between the text.
            Ctrl + J or Ctrl + M: This combination of keys is used to break the line.
            Ctrl + N: Open a new note in the same window.
            Ctrl + Shift + N: Open a new note in a new window.
            Ctrl + P: Open the Print dialog box.
            Ctrl + S: To Save the note.
            Ctrl + Shift + S: Open the Save dialog box so that you can browse a file location to save the note.
            Ctrl + W: Close the Notepad window.
            AltGr or F10: Switch the text cursor into the normal select mode.
            PgUp: Go to the top of the page
            '''
            self.clear()
            self.text_area.insert(0.0, help_text)

    window = tk.Tk()
    note = NotePad(window)
    window.mainloop()

def pan_cardVF():
    import tkinter as tk
    import requests
    from tkinter import messagebox

    def check_pan():
        enter_pan = pan_entry.get()
        url = "https://pan-card-verification1.p.rapidapi.com/v3/tasks/sync/verify_with_source/ind_pan"

        payload = {
            "task_id": "74f4c926-250c-43ca-9c53-453e87ceacd1",
            "group_id": "8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e",
            "data": { "id_number": enter_pan }
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "d2ec0d3958msh9a4c35e841eb4d2p1fb84cjsnffd7656bc39d",
            "X-RapidAPI-Host": "pan-card-verification1.p.rapidapi.com"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                detail = response.json()
                person = detail['result']['source_output']
                first_name = person['first_name']
                last_name = person['last_name']
                aadhar_seeding_status = person['aadhaar_seeding_status']

                messagebox.showinfo("PAN Verification Result",
                                    f"First Name: {first_name}\n"
                                    f"Last Name: {last_name}\n"
                                    f"Linked with Aadhar: {aadhar_seeding_status}")
            else:
                messagebox.showerror("Error", "Failed to fetch PAN details. Please try again later.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Creating the PAN Verification GUI
    pan_window = tk.Toplevel()
    pan_window.title("PAN Verification")
    pan_window.geometry("400x150")

    pan_label = tk.Label(pan_window, text="Enter PAN Number:")
    pan_label.pack(pady=5)

    pan_entry = tk.Entry(pan_window, width=30)
    pan_entry.pack(pady=5)

    check_button = tk.Button(pan_window, text="Check PAN", command=check_pan)
    check_button.pack(pady=5)

    pan_window.mainloop()


def main():
    root = tk.Tk()
    root.title("Project Dashboard")
    root.geometry("450x450")
    root.config(bg="#a0c7e1")
    
    joke_app_button = tk.Button(root, text="JOKE APP", command=open_joke_app, padx=5, pady=5, bg="lightgreen", width=15, height=2)
    joke_app_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    joke_app_label = tk.Label(root, text="Fetch a joke from an API and rate it.")
    joke_app_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    notepad_button = tk.Button(root, text="NOTEPAD", command=open_notepad, padx=5, pady=5, bg="lightgreen", width=15, height=2)
    notepad_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    notepad_label = tk.Label(root, text="Open a simple Notepad application with basic file operations.")
    notepad_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    pan_card_button = tk.Button(root, text="Pan Card Verification", command=pan_cardVF, padx=5, pady=5, bg="lightgreen", width=15, height=2)
    pan_card_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    pan_card_label = tk.Label(root, text="Verify PAN card details using an API.")
    pan_card_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    root.mainloop()

if __name__ == "__main__":
    main()
