from gensim.summarization.summarizer import summarize

# Exemple de texte à résumer
text = """
La bibliothèque Gensim est une bibliothèque Python open-source pour le traitement de texte,
conçue spécifiquement pour travailler avec des corpus de texte de grande taille.
Elle est utilisée pour les applications de traitement du langage naturel (NLP) telles que la modélisation de sujets,
le résumé de texte, et la similarité de documents.
"""

# Résumer le texte
summary = summarize(text, ratio=0.5)  # Le ratio détermine la longueur du résumé
print(summary)

