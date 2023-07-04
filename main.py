# coding: utf-8
 
from tkinter import *
from tkinter.messagebox import showwarning,askokcancel
from PIL import ImageTk, Image
import form_handler

fenetre = Tk()
contenu = Frame(fenetre)


img = Image.open("dino.png")
img.resize((100,60))
img = ImageTk.PhotoImage(img)

# Fonction appelée lorsque le bouton "Quitter" est cliqué
def quitter():
    if askokcancel("Confirmation", "Are you sure you want to quit?"):
        fenetre.destroy()

contenu.grid(column=0, row=0,columnspan=3,rowspan=8)
emptyspace = Label(fenetre, text= " ")
emptyspace.grid(column=2,row=0,padx=100,pady=40)

panel = Label(fenetre, image = img)
panel.grid(column=0,row=0)

label = Label(fenetre, text="Cryptosaurus", bg="blue", fg="white", font=("Harlow Solid Italic",16))
label.grid(column=1,row=0)

CesarForm = form_handler.Form("CAESAR",fenetre,[form_handler.EntryProperties("Message",""),form_handler.EntryProperties("Offset","int")])
bouton_cesar=Button(fenetre, text="Caesar cipher", command=(lambda e = 3 : CesarForm.createForm(e)))

PermForm = form_handler.Form("PERMUTATE",fenetre,[form_handler.EntryProperties("Message",""),form_handler.EntryProperties("Generate random permutation ? (y/n)","YesNo")])
bouton_permu=Button(fenetre, text="Permutations", command=(lambda e = 11 : PermForm.createForm(e)))

RSACForm = form_handler.Form("RSACRYPT",fenetre,[form_handler.EntryProperties("Message","")])
bouton_rsac=Button(fenetre,text="RSA (Crypt)", command=(lambda e = 21 : RSACForm.createForm(e)))

bouton_quitter=Button(fenetre, text="Close", command=quitter)

bouton_cesar.grid(column=1,row=2)
bouton_permu.grid(column=1,row=10)
bouton_rsac.grid(column=1,row=20)
bouton_quitter.grid(column=1,row=30)

# Configurer le placement des widgets dans la fenêtre
fenetre.update_idletasks()  # Mettre à jour la fenêtre pour calculer la taille
largeur_fenetre = fenetre.winfo_width()  # Obtenir la largeur de la fenêtre
#bouton_quitter.place(relx=0.5, rely=1, anchor="s")  # Placer le bouton en bas au milieu

showwarning(title="Before proceeding", message="This program is not to be used to encrypt confidential or sensitive information.\n It is not meant to be used seriously.")

fenetre.mainloop()

