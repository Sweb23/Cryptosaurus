import tkinter as tk

# Fonction appelée lorsque le bouton est cliqué
def afficher_cacher():
    if bouton_afficher_cacher["text"] == "Afficher":
        bouton_afficher_cacher["text"] = "Cacher"
        # Afficher les éléments
        label1.grid(row=0, column=0)
        label2.grid(row=0, column=1)
    else:
        bouton_afficher_cacher["text"] = "Afficher"
        # Cacher les éléments
        label1.grid_remove()
        label2.grid_remove()

# Créer la fenêtre principale
fenetre = tk.Tk()

# Créer les éléments à afficher/cacher
label1 = tk.Label(fenetre, text="Élément 1")
label2 = tk.Label(fenetre, text="Élément 2")

# Créer le bouton "Afficher/Cacher"
bouton_afficher_cacher = tk.Button(fenetre, text="Afficher", command=afficher_cacher)

# Placer le bouton et les éléments dans la grille
bouton_afficher_cacher.grid(row=1, column=0, columnspan=2)

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
