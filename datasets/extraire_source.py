import os
import pandas as pd

# Chemin vers le dossier contenant les fichiers CSV
dossier = '../'

# Numéro de la colonne à extraire (0 pour la première colonne)
indice_colonne_premiere = 0
indice_colonne_derniere = -1

# Nom des fichiers de sortie
fichier_de_sortie_premiere = 'colonne_premiere.csv'
fichier_de_sortie_premiere_et_derniere = 'colonne_premiere_et_derniere.csv'

# Listes pour stocker les données extraites
donnees_premiere_colonne = []
donnees_premiere_et_derniere_colonne = []

# Parcourir tous les fichiers dans le dossier
for fichier in os.listdir(dossier):
    if fichier.endswith('.csv'):
        chemin_fichier = os.path.join(dossier, fichier)
        try:
            # Lire le fichier CSV
            df = pd.read_csv(chemin_fichier)
            
            # Afficher les premières lignes du fichier pour débogage
            print(f"\nContenu de '{fichier}':")
            print(df.head())
            
            # Afficher les noms des colonnes pour vérification
            print(f"Colonnes disponibles dans '{fichier}': {df.columns.tolist()}")
            
            # Vérifier si les indices de colonnes sont valides
            if indice_colonne_premiere < len(df.columns):
                # Extraire la première colonne
                donnees_premiere_colonne += df.iloc[:, indice_colonne_premiere].dropna().tolist()  # Utiliser dropna() pour éviter les valeurs manquantes
            else:
                print(f"Indice de colonne '{indice_colonne_premiere}' invalide dans '{fichier}'.")

            if indice_colonne_derniere < len(df.columns):
                # Extraire la première et la dernière colonne
                donnees_premiere_et_derniere_colonne += df[[df.columns[indice_colonne_premiere], df.columns[indice_colonne_derniere]]].dropna().values.tolist()
            else:
                print(f"Indice de colonne '{indice_colonne_derniere}' invalide dans '{fichier}'.")
                
        except Exception as e:
            print(f"Erreur lors de la lecture de '{fichier}': {e}")

# Créer et sauvegarder les fichiers CSV avec les données extraites
if donnees_premiere_colonne:
    df_premiere = pd.DataFrame({f'Colonne_{indice_colonne_premiere}': donnees_premiere_colonne})
    df_premiere.to_csv(fichier_de_sortie_premiere, index=False)
    print(f"Données de la première colonne sauvegardées dans '{fichier_de_sortie_premiere}'.")

if donnees_premiere_et_derniere_colonne:
    df_premiere_et_derniere = pd.DataFrame(donnees_premiere_et_derniere_colonne, columns=[f'Colonne_{indice_colonne_premiere}', f'Colonne_{indice_colonne_derniere}'])
    df_premiere_et_derniere.to_csv(fichier_de_sortie_premiere_et_derniere, index=False)
    print(f"Données de la première et de la dernière colonne sauvegardées dans '{fichier_de_sortie_premiere_et_derniere}'.")

