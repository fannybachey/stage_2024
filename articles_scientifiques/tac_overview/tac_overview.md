## Points clés de l'article 

1. **Tâche Basée sur Scénario** :
    
    - Un utilisateur pose une question à deux moments différents.
    - La première fois, le système récupère un ensemble d'articles pertinents.
    - Plus tard, le système fournit un résumé de mise à jour avec les nouvelles informations.
     
1. **Évaluation** :
    
    - **Évaluation Automatique** : Scores ROUGE et BE.
    - **Évaluation Manuelle** : Évaluateurs NIST utilisant la méthode Pyramid.
    - Comparaison et corrélation entre évaluations automatiques et manuelles.

2. Task and Data 
![[Pasted image 20240523232311.png]]


![[Pasted image 20240523232259.png]]


2. System Approaches : 

```lua

               +---------------------------------------------+
               |            Résumé Extractif                 |
               +---------------------------------------------+
                             /                     \             +---------------------------------------------+

               ​￼\                |                  /
                ​￼\               |                 /
                 +------------------------------+
                 |    Sélection des Phrases      |
                 ​￼+------------------------------+
                             /   \
              +------------+     +-------------+
              | Classement |     | Clustering  |
              ​￼+------------+     +-------------+
                            |
                +-----------------------------+
                | Post-traitement pour        |
                | améliorer la lisibilité     |
                +-----------------------------+

    +------------------+-----------------+    +---------------------+
    |    Techniques    | Expansion de la |    |   Analyse           |
    | Anti-redondance  |      Requête    |    | Linguistique        |
    +------------------+-----------------+    +---------------------+
             |                |                         |
+------------------+   +------------------+    +----------------------+
| Comparaison     |   | WordNet           |    | Lemmatisation        |
| avec ensemble A |   | Wikipedia         |    | POS tagging          |
+------------------+   +------------------+    +----------------------+
| Maximal         |   | Co-occurrences    |    | NER                  |
| Marginal        |   | de mots           |    | Parsing              |
| Relevance       |   +------------------+    +----------------------+
+------------------+   +------------------+    +----------------------+
| Limitation de la|   |                   |    |                      |
| Similarité      |   |                   |    |                      |
+------------------+   +------------------+    +----------------------+
              \                 |                   /
               \                |                  /
                \               |                 /
                 +------------------------------+
                 |    Sélection des Phrases      |
                 +------------------------------+
                             /   \
              +------------+     +-------------+
              | Classement |     | Clustering  |
              +------------+     +-------------+
                            |
                +-----------------------------+
                | Post-traitement pour        |
                | améliorer la lisibilité     |
                +-----------------------------+

```

**Conclusion** :
    - Les systèmes automatiques montrent une difficulté accrue pour produire des résumés de mise à jour par rapport aux résumés initiaux.
    - Les mesures automatiques ROUGE-2, ROUGE-SU4, et BE-HM ont des corrélations élevées avec les évaluations manuelles, mais ne capturent pas toujours les différences de performance entre résumés initiaux et de mise à jour.

Schéma expansion de la requête : 

```lua
1. Formulation de la Requête Initiale
   +-----------------------------------+
   | "ouragan dommages évacuations"    |
   +-----------------------------------+

              |
              v

2. Identification des Termes Associés
   a. WordNet:
      +-------------------------------+
      | Synonymes: cyclone, tempête   |
      +-------------------------------+

   b. Wikipedia:
      +-------------------------------+
      | Articles associés:            |
      | dépression tropicale, échelle |
      | de Saffir-Simpson             |
      +-------------------------------+

   c. Co-occurrences de Mots:
      +-------------------------------+
      | Contextes fréquents: abri     |
      +-------------------------------+

              |
              v

3. Enrichissement de la Requête
   +-----------------------------------+
   | "ouragan cyclone tempête          |
   | tropicale dommages évacuations    |
   | abri"                             |
   +-----------------------------------+

              |
              v

4. Récupération d'Informations
   +-----------------------------------+
   | Documents plus pertinents         |
   +-----------------------------------+

```


#### TF-IDF 

1. **TF (Term Frequency)** : Mesure combien de fois un mot apparaît dans un document.
2. **IDF (Inverse Document Frequency)** : Mesure à quel point un mot est rare dans l'ensemble de la collection de documents.

En combinant ces deux mesures, le TF-IDF identifie les mots les plus pertinents pour un document spécifique.


4) Evaluation Results 
-> Évaluation avec ROUGE et BE 
Les 1er et 2ème run évalué manuellement 
