from  tkinter  import *
import tkinter as tk
from tkinter.messagebox import *
from tkinter.filedialog import *
import re
from tkinter import messagebox


ecoles = {}
def processing_file():
    text_area.delete(1.0, tk.END)  # Clears the entire content of the Text widget
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt')])
    pattern2 = r'\b(?![._-])(?!.*\-\-)(?!.*\.\.)[A-Za-z0-9._-]+@(?![._-])[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    with open(filename,"r") as f:
        ligne = f.read()
        emails = re.findall(pattern2,ligne)
        print(emails)
    ecoles.clear()
    for email in emails:
        ecole_name = email.split("@")[1].split(".")[0]
        ecoles[ecole_name] = ecoles.get(ecole_name,0) +1
        text_area.insert(tk.END,email+"\n")
        with open(ecole_name+".txt","a") as file:
            file.write(f"{email}\n")
    for widget in container.winfo_children():  # Clear existing labels before updating
        widget.destroy()
    for ecole,nbremails in ecoles.items():
        label= Label(container,text=f"university {ecole} : {nbremails} Emails availble")
        label.pack()
    container.pack()


def display_about():
    messagebox.showinfo("About", "For contact Anass-nabil.vercel.app")

window  = Tk("Email validator | Email Spliter")
window.title("Email validator | Email Spliter")
icon = tk.PhotoImage(file="logo.png")
window.iconphoto(True,icon)
fixed_width = 450
fixed_height = 600
window.geometry(f"{fixed_width}x{fixed_height}")

l = LabelFrame(window, text="Preprocessing Emails file", padx=20, pady=20, height=50, width=50)
l.pack(fill="both", expand="yes")

Button(l,text="Upload file",command=processing_file).pack()
# Create a Text widget
text_area = tk.Text(l, height=10, width=30)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar
scrollbar = tk.Scrollbar(l, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)







def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Upload", command=processing_file)
menu1.add_separator()
menu1.add_command(label="Quitter", command=window.quit)
menubar.add_cascade(label="Fichier", menu=menu1)



menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A ", command=alert)
menubar.add_cascade(label="About", command=display_about)

window.config(menu=menubar)


container = Frame(window)

# window.resizable(False,False)
window.mainloop()
print(dir(window))