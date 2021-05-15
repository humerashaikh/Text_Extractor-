import tkinter as tk
from PIL  import  Image ,ImageTk
from tkinter.filedialog import askopenfile
import PyPDF2
root=tk.Tk()
canvas=tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3, rowspan=3)
# open Logo
logo=Image.open('logo.png')
logo=ImageTk.PhotoImage(logo)
logo_lable=tk.Label(image=logo)
logo_lable.image=logo
logo_lable.grid(column=1,row=0)

#instruction
instruction=tk.Label(root,text="select PDF File , To Extract text ",font="Raleway" )
instruction.grid(columnspan =3,column=0,row=1)
# Button Function
def open_file():
    browse_text.set("loading")
    file=askopenfile(parent=root, mode='rb', title ="choose a file ", filetype=[("Pdf file,","*.pdf")])
    if file:

        read_pdf=PyPDF2.PdfFileReader(file)
        page=read_pdf.getPage(1)
        page_content=page.extractText()
        #textbox
        text_box=tk.Text(root,height=10,width=50,padx=15,pady=15)
        text_box.insert(2.0,page_content)
        text_box.tag_add("center ",1.0,"end")
        text_box.grid(column=1,row=3)
        browse_text.set("Browse")
# browse Button
browse_text=tk.StringVar()
browse_btn=tk.Button(root, textvariable=browse_text,command=lambda :open_file(),font="Raleway",bg="#20bebe",height=2,width=15,fg="white")
browse_text.set("Browse")
browse_btn.grid(column=1,row=2)
root.mainloop()