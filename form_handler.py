# coding: utf-8

from tkinter import *
from tkinter import filedialog
import chiffrement_cesar
import chiffrement_RSA
from tkinter.messagebox import showwarning
import os
import sys
import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Obtenir le chemin absolu du dossier contenant le module
chemin_dossier_module = os.path.abspath(os.path.join(os.path.dirname(__file__), 'perm'))

# Ajouter le chemin du dossier à sys.path
sys.path.append(chemin_dossier_module)

import chiffrement_permutation as chp

# Obtenir le chemin absolu du dossier contenant le module
chemin_dossier_module = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bij'))

# Ajouter le chemin du dossier à sys.path
sys.path.append(chemin_dossier_module)

import chiffrement_bijection as cb

CRYPT_TYPES = ("CAESAR","PERMUTATE","BIJECTION","RSACRYPT","RSADECRYPT","ZTON","SEQUENCE")

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
        
    def script_bijection_crypt(self,values,bij):
        try:
            if values[1] == "y":
                with open('bij/custom_alphabet.json','r') as alpha:
                    M = json.load(alpha)
                    for l in M:
                        if l != int(l):
                            raise Exception("Integer list required")
                C = cb.chiffrement_bijection(M,bij(*values[2:]))
            elif values[1] == "n":
                print("OK")
                C = cb.chiffrement_bijection(cb.B,bij(*values[2:]))
                print("OKK")
            path_fichier = filedialog.asksaveasfilename(defaultextension=".json",initialfile="mapped_alphabet",parent=self.window,
                                             title="Save mapped alphabet",
                                                        filetypes=[("All files",""),("Javascript object notation (JSON)",".json")])
            with open(path_fichier,'w') as f:
                f.write(json.dumps(C))
            msg_cry = ""
            let_cry = 0
            
            for lettre in values[0]:
                if lettre.isalpha():
                    let_cry = C[cb.A.index(lettre.upper())]
                    msg_cry+= str(let_cry) + " & "
                else:
                    msg_cry += lettre + " & "
            
            Label(self.window,text="To decrypt, send the message and mapped alphabet to reciever").grid(row=4,column=2)
            
            Label(self.window,text="Result : ").grid(row=5,column=2)
            text_box2 = Text(self.window, height=5, width=25, wrap="word")
            text_box2.insert(END, msg_cry)
            text_box2.grid(row=6,column=2)
        except:
            showwarning(title="Error", message="Something went wrong when computing the new message.")

    def script_bijection_decrypt(self,values,bij):
        try:
            path_alpha = filedialog.askopenfilename(defaultextension=".json",initialfile="custom_alphabet.json",parent=self.window,
                                             title="Open custom alphabet file",
                                                        filetypes=[("All files",""),("Javascript object notation (JSON)",".json")])
            with open(path_alpha,'r') as f:
                print("OKK")
                C = json.load(f)
                
                for l in C:
                    if l != int(l):
                        raise Exception("Integer list required")

            
            D = cb.dechiffrement_bijection(C,bij(*values[2:]))
            print("OK")

            msg_dec = values[0].split(" & ")
            
            
            msg_fin = ""
            el_decr = 0
            for el in msg_dec:
                if cb.is_number(el):
                    
                    el_decr = D[C.index(float(el))]
                    msg_fin += cb.A[int(el_decr)]
                else:
                    msg_fin += el
            
            Label(self.window,text="Result : ").grid(row=5,column=2)
            text_box2 = Text(self.window, height=5, width=25, wrap="word")
            text_box2.insert(END, msg_fin)
            text_box2.grid(row=6,column=2)
        except:
            showwarning(title="Error", message="Something went wrong when computing the new message.")

        
    def checkValues(self):
        values = []
        for e in self.entries:
            val = e.textVar.get()
            #print(val)
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
                    case "nonZero":
                        if float(val) != 0:
                            values += [val]
                        else:
                            raise Exception("Non zero float required")
                    case "float":
                        if float(val) == val:
                            values += [val]
                        else:
                            raise Exception("Real number required")
                    case other:
                        pass
                #print(values[len(values) - 1])
            except:
                showwarning(title="Error", message="Something went wrong when processing your form.")
                

        match self.crypt:
            case "CAESAR":
                try:
                    msg_crypt = chiffrement_cesar.chiffrement(values[0],int(values[1]))
                    Label(self.window,text="Your crypted message : ").grid(row=6,column=2)
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
            case "ZTON":
                try:
                    if values[1] == "y":
                        with open('bij/custom_alphabet.json','r') as alpha:
                            M = json.load(alpha)
                            for l in M:
                                if l != int(l):
                                    raise Exception("Integer list required")
                        C = cb.chiffrement_bijection(M,cb.z_to_n)
                    elif values[1] == "n":
                        #print("OK")
                        C = cb.chiffrement_bijection(cb.B,cb.z_to_n)
                        #print("OKK")
                    path_fichier = filedialog.asksaveasfilename(defaultextension=".json",initialfile="mapped_alphabet",parent=self.window,
                                                     title="Save mapped alphabet",
                                                                filetypes=[("All files",""),("Javascript object notation (JSON)",".json")])
                    with open(path_fichier,'w') as f:
                        f.write(json.dumps(C))
                    msg_cry = ""
                    let_cry = 0
                    
                    for lettre in values[0]:
                        if lettre.isalpha():
                            let_cry = C[cb.A.index(lettre.upper())]
                            msg_cry+= str(let_cry) + " & "
                        else:
                            msg_cry += lettre + " & "
                    
                    Label(self.window,text="To decrypt, send the message and mapped alphabet to reciever").grid(row=4,column=2)
                    
                    Label(self.window,text="Result : ").grid(row=5,column=2)
                    text_box2 = Text(self.window, height=5, width=25, wrap="word")
                    text_box2.insert(END, msg_cry)
                    text_box2.grid(row=6,column=2)
                except:
                    showwarning(title="Error", message="Something went wrong when computing the new message.")
            case "NTOZ":
                try:
                    path_alpha = filedialog.askopenfilename(defaultextension=".json",initialfile="custom_alphabet.json",parent=self.window,
                                                     title="Open custom alphabet file",
                                                                filetypes=[("All files",""),("Javascript object notation (JSON)",".json")])
                    with open(path_alpha,'r') as f:
                        print("OKK")
                        C = json.load(f)
                        
                        for l in C:
                            if l != int(l):
                                raise Exception("Integer list required")

                    
                    D = cb.dechiffrement_bijection(C,cb.n_to_z)
                    print("OK")

                    msg_dec = values[0].split(" & ")
                    
                    
                    msg_fin = ""
                    el_decr = 0
                    for el in msg_dec:
                        if cb.is_number(el):
                            
                            el_decr = D[C.index(float(el))]
                            msg_fin += cb.A[int(el_decr)]
                        else:
                            msg_fin += el
                    
                    Label(self.window,text="Result : ").grid(row=5,column=2)
                    text_box2 = Text(self.window, height=5, width=25, wrap="word")
                    text_box2.insert(END, msg_fin)
                    text_box2.grid(row=6,column=2)
                except:
                    showwarning(title="Error", message="Something went wrong when computing the new message.")
            case "LIN":
                self.script_bijection_crypt(values,cb.lin_coefs)
                    
#======================================================================
#Cryptage RSA : génération de clés et sauvegarde ds un fichier
#======================================================================
            case "RSACRYPT":
                try:
                    pu_key,pr_key = chiffrement_RSA.generer_cles_RSA()
                    msg_crypt = chiffrement_RSA.chiffrer_RSA(values[0],pu_key)
                    

                    path_fichier = filedialog.asksaveasfilename(defaultextension=".txt",initialfile="RSA_Result",parent=self.window,
                                                     title="Save keys and message",
                                                                filetypes=[("All files",""),("Text files",".txt")])
                    if path_fichier != "":
                        with open(path_fichier,mode="w",encoding='utf-8') as f:
                            f.write("Public key : \n")
                            f.write(pu_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PublicFormat.SubjectPublicKeyInfo).decode('utf-8'))
                            f.write("\n \n")
                            f.write("Private key : \n")
                            f.write(pr_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                         format=serialization.PrivateFormat.PKCS8,
                                                         encryption_algorithm=serialization.NoEncryption()).decode('utf-8'))
                            f.write("\n \n")
                            f.write("Your crypted message : \n")
                            f.write(str(msg_crypt))
                        
                            new_path_key = os.path.join(os.path.dirname(path_fichier),"private_key.pem")
                            new_path_message = os.path.join(os.path.dirname(path_fichier),"crypted_message.bin")
                            # Écrire la clé privée dans un fichier
                            with open(new_path_key, "wb") as fichier_cle_privee:
                                fichier_cle_privee.write(pr_key.private_bytes(
                                    encoding=serialization.Encoding.PEM,
                                    format=serialization.PrivateFormat.PKCS8,
                                    encryption_algorithm=serialization.NoEncryption()
                                ))
                            with open(new_path_message,"wb") as fichier_msg:
                                fichier_msg.write(msg_crypt)
                            
                        Label(self.window,
                              text="See txt file for results.\nTo decrypt, give the files private_key and crypted_message to the reciever.").grid(row=9,
                                                                                                                                                column=2)

                except:
                    showwarning(title="Error", message="Something went wrong when computing the new message.")
#======================================================================
#Decryptage RSA : Lecture de la clé privée et du message
#======================================================================              
            case "RSADECRYPT":
                try:
                    path_key = filedialog.askopenfilename(defaultextension=".pem",initialfile="private_key.pem",parent=self.window,
                                                     title="Open private key file",
                                                                filetypes=[("All files",""),("PEM files",".pem")])
                    path_msg = filedialog.askopenfilename(defaultextension=".bin",initialfile="crypted_message.bin",parent=self.window,
                                                     title="Open message file",
                                                                filetypes=[("All files",""),("Binary files",".bin")])
                    with open(path_key, "rb") as fichier_cle_privee:
                        cle_privee = serialization.load_pem_private_key(
                            fichier_cle_privee.read(),
                            password=None,
                            backend=default_backend()
                        )
                        with open(path_msg, "rb") as fichier_msg:
                            msg_crypt = fichier_msg.read()
                        
                            msg = chiffrement_RSA.dechiffrer_RSA(msg_crypt,cle_privee)
                        Label(self.window,text="Decrypted message : ").grid(row=10,column=2)
                        text_box3 = Text(self.window, height=5, width=25, wrap="word")
                        text_box3.insert(END, msg)
                        text_box3.grid(row=11,column=2)
                except:
                    showwarning(title="Error", message="Something went wrong.")
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

        

