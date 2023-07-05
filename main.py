# coding: utf-8
 
from tkinter import *
from tkinter.messagebox import showwarning,askokcancel
from PIL import ImageTk, Image
import form_handler
import os, sys

# Obtenir le chemin absolu du dossier contenant le module
chemin_dossier_module = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bij'))

# Ajouter le chemin du dossier à sys.path
sys.path.append(chemin_dossier_module)

import bij_handler as bh

fenetre = Tk()
contenu = Frame(fenetre)


img = Image.open("dino.png")
img = ImageTk.PhotoImage(img)

# Fonction appelée lorsque le bouton "Quitter" est cliqué
def quitter():
    if askokcancel("Confirmation", "Are you sure you want to quit?"):
        fenetre.destroy()

def open_bij():
    bij_window = Toplevel(fenetre)
    bh.bij_display(bij_window)


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

RSADForm = form_handler.Form("RSADECRYPT",fenetre,[])
#form_handler.EntryProperties("Message",""),form_handler.EntryProperties("Private key","")
bouton_rsad = Button(fenetre,text="RSA (Decrypt)", command=(lambda e = 31 : RSADForm.createForm(e)))

bouton_bij = Button(fenetre,text="Bijection",command=open_bij)

bouton_quitter=Button(fenetre, text="Close", command=quitter)

bouton_cesar.grid(column=1,row=2)
bouton_permu.grid(column=1,row=10)
bouton_rsac.grid(column=1,row=20)
bouton_rsad.grid(column=1,row=30)
bouton_bij.grid(column=1,row=40)
bouton_quitter.grid(column=1,row=50)

# Configurer le placement des widgets dans la fenêtre
fenetre.update_idletasks()  # Mettre à jour la fenêtre pour calculer la taille
largeur_fenetre = fenetre.winfo_width()  # Obtenir la largeur de la fenêtre
#bouton_quitter.place(relx=0.5, rely=1, anchor="s")  # Placer le bouton en bas au milieu

showwarning(title="Before proceeding", message="This program is not to be used to encrypt confidential or sensitive information.\n It is not meant to be used seriously.")

fenetre.mainloop()

