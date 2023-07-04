from tkinter import *
import chiffrement_cesar
from tkinter.messagebox import showwarning
import os
import sys
import json

# Obtenir le chemin absolu du dossier contenant le module
chemin_dossier_module = os.path.abspath(os.path.join(os.path.dirname(__file__), 'perm'))

# Ajouter le chemin du dossier à sys.path
sys.path.append(chemin_dossier_module)

import chiffrement_permutation as chp

CRYPT_TYPES = ("CAESAR","PERMUTATE","BIJECTION","RSA","SEQUENCE")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class EntryProperties:
    textVar = ""
    
    def __init__(self,name, cond=""):
        self.name = name
        self.cond = cond
        
        
class Form:
    form = []
    def __init__(self,crypt,window,entries=[],disp=False):
        self.entries = entries
        self.crypt = crypt
        self.disp = disp
        self.window = window
        
        
    def checkValues(self):
        values = []
        for e in self.entries:
            val = e.textVar.get()
            try:
                match e.cond:
                    case "":
                        values += [val]
                    case "int":
                        if is_number(val) and (int(val) == float(val)):
                            values += [int(val)]
                        else:
                            raise Exception("Not a number or not an integer")
                    case "YesNo":
                        if val == "y" or val == "n":
                            values += [val]
                        else:
                            raise Exception("y/n answer required")
                    case other:
                        pass
            except:
                showwarning(title="Error", message="Something went wrong. Please double check your input.")
                

        match self.crypt:
            case "CAESAR":
                try:
                    msg_crypt = chiffrement_cesar.chiffrement(values[0],int(values[1]))
                    Label(self.window,text="Your crypted message : ").grid(row=6,column=2)
                    #Entry(self.window,state="readonly",textvariable=StringVar(value=msg_crypt)).grid(row=7,column=2)
                    text_box = Text(self.window, height=5, width=25, wrap="word")
                    text_box.insert(END, msg_crypt)
                    text_box.grid(row=7,column=2)
                except:
                    showwarning(title="Error", message="Something went wrong. Please double check your input.")
            case "PERMUTATE":
                try:
                    if values[1] == "y":
                        M = chp.perm_alea().tolist()
                        msg_crypt,alpha = chp.chiffrement_permutation(values[0],M)
                    elif values[1] == "n":
                        # Charger le fichier JSON
                        with open('perm\\custom_permutation.json', 'r') as fichier:
                            M = json.load(fichier)
                        msg_crypt,alpha = chp.chiffrement_permutation(values[0],chp.alpha_to_perm(M))
                    
                    Label(self.window,text="Generated permutation : ").grid(row=4,column=2)
                    text_box = Text(self.window, height=5, width=25, wrap="word")
                    text_box.insert(END, M)
                    text_box.grid(row=5,column=2)
                    
                    Label(self.window,text="New alphabet : ").grid(row=6,column=2)
                    text_box2 = Text(self.window, height=5, width=25, wrap="word")
                    text_box2.insert(END, alpha)
                    text_box2.grid(row=7,column=2)
                    
                    Label(self.window,text="Your crypted message : ").grid(row=8,column=2)
                    text_box3 = Text(self.window, height=5, width=25, wrap="word")
                    text_box3.insert(END, msg_crypt)
                    text_box3.grid(row=9,column=2)
                except:
                    showwarning(title="Error", message="Something went wrong when computing the new message.")
            case other:
                pass
            
    def createForm(self,firstRow=0):
        if not self.disp:
            self.disp=True
            print("Affichage\n")
            for e in self.entries:
                self.form += [Label(self.window,text = e.name)]
                self.form[len(self.form)-1].grid(row=firstRow,column=1)
                firstRow += 1
                e.textVar = StringVar()
                self.form += [Entry(self.window, textvariable=e.textVar)]
                self.form[len(self.form)-1].grid(row=firstRow,column=1)
                firstRow +=1
                
            # Create the button that handles user input
            self.form += [Button(self.window, text = "Crypt", command=self.checkValues)]
            self.form[len(self.form)-1].grid(row=firstRow,column=1)
        
        else:
            self.disp=False
            print("Désaffichage\n")
            for f in self.form:
                f.grid_remove()
            self.form = []

        

