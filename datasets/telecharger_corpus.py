from datasets import load_dataset
import pandas as pd

# Charger le dataset CNN/DailyMail en spécifiant la version
dataset = load_dataset('cnn_dailymail', '3.0.0')

# Séparer les données en ensembles d'entraînement, de développement (dev) et de test
train_data = dataset["train"]
dev_data = dataset["validation"]
test_data = dataset["test"]

# Fonction pour sauvegarder les données dans un fichier CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Sauvegarder les données dans des fichiers CSV
save_to_csv(train_data, "Corpus/cnn_dailymail_train.csv")
save_to_csv(dev_data, "Corpus/cnn_dailymail_dev.csv")
save_to_csv(test_data, "Corpus/cnn_dailymail_test.csv")

print("Données sauvegardées avec succès en fichiers CSV.")

