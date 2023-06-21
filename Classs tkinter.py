from tkinter import*
from tkinter import messagebox
root=Tk()

root.title("classs")
root.geometry("1000x1000")

class create_element:
    def __init__(self):
        print("this is a create element class")
    def element(self):
        label=Label(root,text="a new label has been created for this class",fg="#059908")
        label.pack()
        bto=Button(root,text="Button",command=self.message)
        bto.pack()
    def message(self):
        messagebox.showinfo("info","class button clicked")
        
obj=create_element() 
       

btn=Button(root,text="Click to create label and button",command=obj.element)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
