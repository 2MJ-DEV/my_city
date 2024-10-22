import tkinter as tk
from PIL import ImageTk, Image
import os

# Créer une fenêtre principale
root = tk.Tk()
root.title("Logo des villes")

# Dictionnaire pour stocker les noms des villes et les chemins des logos
city_logos = {
    "Lubumbashi": "Lubumbashi.jpg",
    "Kolwezi": "kolwezi.jpg",
    "Kasumbalesa": "kasumbalesa.jpg"
}

# Fonction pour afficher le logo
def show_logo():
    city = city_entry.get().capitalize()
    if city in city_logos:
        logo_path = city_logos[city]
        if os.path.exists(logo_path):
            img = Image.open(logo_path)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)  # Redimensionner l'image
            logo_img = ImageTk.PhotoImage(img)
            logo_label.config(image=logo_img)
            logo_label.image = logo_img
        else:
            result_label.config(text="Logo introuvable.")
    else:
        result_label.config(text="Ville non trouvée.")

# Champ pour entrer le nom de la ville
city_entry = tk.Entry(root)
city_entry.pack(pady=10)

# Bouton pour afficher le logo
show_button = tk.Button(root, text="Afficher le logo", command=show_logo)
show_button.pack(pady=5)

# Label pour afficher le résultat
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Label pour afficher l'image du logo
logo_label = tk.Label(root)
logo_label.pack(pady=10)

# Lancer la boucle principale
root.mainloop()
