from Tkinter import *

root_widget = Tk()
root_widget2 = Tk()
var_label_text = StringVar()

entry_text = Entry()
entry_text2 = Entry()
btn_ok = Button(text='ok', command=lambda: var_label_text.set(entry_text.get()))


def main():
    root_widget.geometry("300x100")
    root_widget.title("Simple GUI Demo")
    root_widget2.geometry ("150x100")


    var_label_text.set("Display your full name here")  
    lbl_name = Label(root_widget, textvariable=var_label_text)
    lbl_name.grid(row=1, column=0)  

    
    Label(text="First").grid(row=2, column=0) 
    Label(text="Last").grid(row=3, column=0)







    entry_text.insert(0, "Type first name.")
    entry_text.grid(row=4, column=1)

    entry_text2.insert(0, "Type Last Name")    
    entry_text2.grid()

    btn_ok.grid()

    root_widget.mainloop()

if __name__ == '__main__':
    main()    