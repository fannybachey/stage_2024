import os
from datasets import load_dataset

# Spécifiez le répertoire de téléchargement
output_directory = "../../cnn_dm"

# Créer le répertoire s'il n'existe pas
os.makedirs(output_directory, exist_ok=True)

# Charger le dataset CNN/DailyMail avec une version de configuration spécifique
dataset = load_dataset("cnn_dailymail", "3.0.0")

# Afficher les clés du dataset pour voir les splits disponibles
print("Dataset splits:", dataset.keys())

# Obtenir des informations sur le dataset
print("Dataset information:", dataset)

# Accéder au split d'entraînement
train_data = dataset['train']

# Obtenir le nombre d'échantillons dans le split d'entraînement
print(f"Number of training samples: {len(train_data)}")

# Obtenir les noms des colonnes
print(f"Column names: {train_data.column_names}")

# Enregistrer les articles et leurs résumés dans des fichiers texte
for i, sample in enumerate(train_data):
    article_path = os.path.join(output_directory, f"article_{i}.txt")
    summary_path = os.path.join(output_directory, f"summary_{i}.txt")
    
    with open(article_path, 'w', encoding='utf-8') as article_file:
        article_file.write(sample['article'])
    
    with open(summary_path, 'w', encoding='utf-8') as summary_file:
        summary_file.write(sample['highlights'])

    # Optionnel: Afficher les premiers articles et résumés pour vérification
    if i < 5:
        print(f"Saved article and summary {i}")
        print("Article:", sample['article'])
        print("Summary:", sample['highlights'])

