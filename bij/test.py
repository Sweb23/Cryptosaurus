import tkinter as tk
from PIL import Image, ImageTk

# Créez une fenêtre principale
root = tk.Tk()

# Chargez l'image à partir du dossier "img"
image_path = "img/fleches.png"
image = Image.open(image_path)

# Convertissez l'image en un format compatible avec tkinter
photo = ImageTk.PhotoImage(image)

# Créez le bouton avec l'image
bouton = tk.Button(root, image=photo)
bouton.pack()

root.mainloop()
