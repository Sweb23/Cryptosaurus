from tkinter import *
import chiffrement_cesar
from time import sleep
from tkinter.messagebox import showwarning

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
                    case other:
                        pass
            except:
                errLabel = Label(self.window,text="Something went wrong.")
                errLabel.grid(row=6,column=2)
                sleep(0.5)
                errLabel.grid_remove()
                

        match self.crypt:
            case "CAESAR":
                try:
                    msg_crypt = chiffrement_cesar.chiffrement(values[0],int(values[1]))
                    Label(self.window,text="Your crypted message : ").grid(row=6,column=2)
                    Entry(self.window,state="readonly",textvariable=StringVar(value=msg_crypt)).grid(row=7,column=2)
                except:
                    showwarning(title="Error", message="Something went wrong. Please double check your input.")
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

        

