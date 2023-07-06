from tkinter import *
import os, sys
from PIL import ImageTk, Image


# Obtenir le chemin absolu du dossier contenant le module
chemin_dossier_module = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Ajouter le chemin du dossier à sys.path
sys.path.append(chemin_dossier_module)
globalTopLevel = None
import form_handler as fh
ZtonForm = fh.Form("ZTON",globalTopLevel,[fh.EntryProperties("Message",""),
                                          fh.EntryProperties("Use custom alphabet ? (y/n)","YesNo")])

NtozForm = fh.Form("NTOZ",globalTopLevel,[fh.EntryProperties("Crypted Message","")])

LinForm = fh.Form("LIN",globalTopLevel,[fh.EntryProperties("Message",""),
                                        fh.EntryProperties("Use custom alphabet ? (y/n)","YesNo"),
                                        fh.EntryProperties("a","nonZero"),fh.EntryProperties("b","float")])

LirForm = fh.Form("LIR",globalTopLevel,[fh.EntryProperties("Crypted Message",""),
                                        fh.EntryProperties("a","nonZero"),
                                        fh.EntryProperties("b","float")])

ExpForm = fh.Form("EXP",globalTopLevel,[fh.EntryProperties("Message",""),
                                        fh.EntryProperties("Use custom alphabet ? (y/n)","YesNo"),
                                        fh.EntryProperties("a","nonZero"),fh.EntryProperties("b","nonZero"),
                                        fh.EntryProperties("c","float"),fh.EntryProperties("d","float")])

LogForm = fh.Form("LOG",globalTopLevel,[fh.EntryProperties("Crypted Message",""),
                                        fh.EntryProperties("a","nonZero"),fh.EntryProperties("b","nonZero"),
                                        fh.EntryProperties("c","float"),fh.EntryProperties("d","float")])

PuiForm = fh.Form("PUI",globalTopLevel,[fh.EntryProperties("Message",""),
                                        fh.EntryProperties("Use custom alphabet ? (y/n)","YesNo"),
                                        fh.EntryProperties("y","nonZero"),
                                        fh.EntryProperties("a","nonZero"),fh.EntryProperties("b","nonZero"),
                                        fh.EntryProperties("c","float"),fh.EntryProperties("d","float")])

PurForm = fh.Form("PUR",globalTopLevel,[fh.EntryProperties("Crypted Message",""),fh.EntryProperties("y","nonZero"),
                                        fh.EntryProperties("a","nonZero"),fh.EntryProperties("b","nonZero"),
                                        fh.EntryProperties("c","float"),fh.EntryProperties("d","float")])

def create_img(path):
    # Chargez l'image à partir du dossier "img"
    image_path = path
    image = Image.open(image_path)
    image = image.resize((335,97))

    # Convertissez l'image en un format compatible avec tkinter
    photo = ImageTk.PhotoImage(image)
    #print(str(photo.width()) + " " + str(photo.height()))
    return photo

def bij_display(toplevel):
    globalTopLevel = toplevel
    print(os.getcwd())
    
    emptyspace = Label(toplevel, text= "Crypt")
    emptyspace.grid(column=0,row=0,padx=100,pady=40)
    im1 = create_img("bij/img/fleches.png")
    Label(toplevel, image=im1).grid(column=1,row=0)
    
    emptyspace = Label(toplevel, text= "Decrypt")
    emptyspace.grid(column=2,row=0,padx=100,pady=40)
    
    im2 = create_img("bij/img/fun1.png")
    Button(toplevel, image=im2, command=(lambda e = ZtonForm : toplevelForm(e))).grid(column=0,row=1)

    im3 = create_img("bij/img/fun2.png")
    Button(toplevel, image=im3, command=(lambda e = NtozForm : toplevelForm(e))).grid(column=2,row=1)
    
    im4 = create_img("bij/img/exp.png")
    Button(toplevel, image=im4, command=(lambda e = ExpForm : toplevelForm(e))).grid(column=0,row=2)
    
    im5 = create_img("bij/img/log.png")
    Button(toplevel, image=im5, command=(lambda e = LogForm : toplevelForm(e))).grid(column=2,row=2)
    
    im6 =create_img("bij/img/lin.png")
    Button(toplevel, image=im6, command=(lambda e = LinForm : toplevelForm(e))).grid(column=0,row=3)
    
    im7 = create_img("bij/img/lir.png")
    Button(toplevel, image=im7, command=(lambda e = LirForm : toplevelForm(e))).grid(column=2,row=3)
    
    im8 = create_img("bij/img/pui.png")
    Button(toplevel, image=im8, command=(lambda e = PuiForm : toplevelForm(e))).grid(column=0,row=4)
    
    
    im9 = create_img("bij/img/pur.png")
    Button(toplevel, image=im9, command=(lambda e = PurForm : toplevelForm(e))).grid(column=2,row=4)
    
    Button(toplevel, text="Close",command=toplevel.destroy).grid(column=1,row=11)
    
    toplevel.mainloop()
    
def toplevelForm(form):
    form_window = Toplevel(globalTopLevel)
    form.window = form_window
    form.createForm()
    Button(form_window, text="Close",command=form_window.destroy).grid(column=1,row=21)

    form_window.mainloop()