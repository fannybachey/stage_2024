
Ligne de commande pour lancer l'application : 
```bash 
streamlit run summvis.py -- --path examples/wikinews/wikinews.cache
```

## Remarques : 
- Utilisation de Streamlit : permet de créer facilement des apps. 
- Comparaiosn possible entre input et le document source 

Overview : 

![[Pasted image 20240606154515.png]]

Différents résumé : 
- résumé de référence 
- BART (CNNDM-trained)
- BART (XSUM-trained)
- PEGASUS (CNNDM-trained)
- PEGASUS (XSUM-trained)


# Ce que contient l'interface

![[Pasted image 20240606155019.png]]

**Dans la barre de recherche de gauche :** 
- À partir de quoi on veut faire la comparaison (document ou résumé de référence)
- Quels modèles de résumé automatique on test 
- type de similarité sémantique : contextuelle ou statique 
- curseur pour ajuster le seuil de similarité sémantique (pour le mot ou pour la phrase)
- Un curseur permettant de définir le nombre maximal de résultats de similarité sémantique à afficher
- Layout : Vertical/Horizontal 
- stop-words

**Main :** 
- file/ Index 
- Annotation : Des onglets pour afficher des informations sur le chevauchement de n-grammes, les nouveaux mots, et les nouvelles entités dans les résumés par rapport au document source. (Possible d'activé et de désactivé)
- Source document : document source 
- Summary : Les différents résumés générés s'affichent dans une petite fenêtre 


# Comment on fait pour mettre des données 


# Analyse

3 niveaux d'analyse : 
- Model Analysis : by comparing the source document with generated summaries, SUMMVIS provides insights into a model’s ability to abstract and faithfully retain information present in the document.

- Data Analysis : By comparing the source document with the reference summary, SUMMVIS helps determine the degree to which the reference summary itself is abstractive and factually consistent with the source document.

- Evaluation Analysis: By comparing the reference summary with the generated summary, SUMMVIS surfaces the word- and phrase-level relationships that form the basis of automated evaluation metrics such as ROUGE and BERTScore.
