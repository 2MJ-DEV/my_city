# Importer la bibliothèque tkinter pour créer une interface graphique
import tkinter as tk

# Importer les classes ImageTk et Image de la bibliothèque Pillow pour le traitement des images
from PIL import ImageTk, Image

# Importer le module os pour interagir avec le système de fichiers
import os

# Créer une fenêtre principale pour l'application
root = tk.Tk()
# Définir le titre de la fenêtre principale
root.title("Logo des villes")

# Dictionnaire pour stocker les noms des villes et les chemins des fichiers image des logos
city_logos = {
    "Lubumbashi": "Lubumbashi.jpg",   # Chemin vers le logo de Lubumbashi
    "Kolwezi": "kolwezi.jpg",          # Chemin vers le logo de Kolwezi
    "Kasumbalesa": "kasumbalesa.jpg"  # Chemin vers le logo de Kasumbalesa
}

# Fonction pour afficher le logo correspondant à la ville saisie
def show_logo():
    # Récupérer le texte saisi par l'utilisateur, en mettant la première lettre en majuscule
    city = city_entry.get().capitalize()
    
    # Vérifier si la ville saisie est présente dans le dictionnaire
    if city in city_logos:
        # Obtenir le chemin du logo à partir du dictionnaire
        logo_path = city_logos[city]
        
        # Vérifier si le fichier image du logo existe
        if os.path.exists(logo_path):
            # Ouvrir l'image du logo
            img = Image.open(logo_path)
            # Redimensionner l'image à 150x150 pixels
            img = img.resize((150, 150), Image.Resampling.LANCZOS)  
            # Convertir l'image pour l'afficher dans Tkinter
            logo_img = ImageTk.PhotoImage(img)
            # Mettre à jour le label pour afficher l'image du logo
            logo_label.config(image=logo_img)
            # Garder une référence à l'image pour éviter qu'elle ne soit détruite par le garbage collector
            logo_label.image = logo_img
        else:
            # Afficher un message d'erreur si le logo n'est pas trouvé
            result_label.config(text="Logo introuvable.")
    else:
        # Afficher un message d'erreur si la ville saisie n'est pas reconnue
        result_label.config(text="Ville non trouvée.")

# Champ de saisie pour que l'utilisateur entre le nom de la ville
city_entry = tk.Entry(root)
# Ajouter le champ de saisie à la fenêtre et ajouter un espacement vertical
city_entry.pack(pady=10)

# Bouton pour afficher le logo de la ville saisie
show_button = tk.Button(root, text="Afficher le logo", command=show_logo)
# Ajouter le bouton à la fenêtre et ajouter un espacement vertical
show_button.pack(pady=5)

# Label pour afficher le message de résultat (vide au départ)
result_label = tk.Label(root, text="")
# Ajouter le label à la fenêtre et ajouter un espacement vertical
result_label.pack(pady=10)

# Label pour afficher l'image du logo (vide au départ)
logo_label = tk.Label(root)
# Ajouter le label à la fenêtre et ajouter un espacement vertical
logo_label.pack(pady=10)

# Lancer la boucle principale de l'interface graphique pour écouter les événements
root.mainloop()
