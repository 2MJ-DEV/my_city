# my_city

# Affichage de logos des villes avec Tkinter et Pillow

Ce projet permet d'afficher le logo d'une ville en fonction de la saisie de l'utilisateur dans une interface graphique créée avec Tkinter. Les logos sont redimensionnés pour s'adapter à une fenêtre de 150x150 pixels à l'aide de la bibliothèque `Pillow`.

## Fonctionnalités

- L'utilisateur peut entrer le nom d'une ville (exemple : "Lubumbashi", "Kolwezi", "Kasumbalesa").
- Si la ville est reconnue, le logo correspondant est affiché.
- Les logos sont redimensionnés à 150x150 pixels pour s'adapter à la fenêtre.
- Gestion des erreurs si la ville saisie n'existe pas ou si le fichier image du logo est introuvable.

## Prérequis

- Python 3.x
- Bibliothèques :
  - Tkinter (inclus dans la plupart des distributions Python)
  - Pillow (pour le traitement des images)
## Auteur

https://github.com/2MJ-DEV

Pour installer `Pillow`, utilisez la commande suivante :

```bash
pip install pillow
