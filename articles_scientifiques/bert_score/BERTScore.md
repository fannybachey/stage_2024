
BERTScore est une méthode d'évaluation qui mesure la similarité sémantique entre des phrases ou des textes. Voici une explication détaillée :

### Semantic Similarity vs Token Level Syntactical Similarity

1. **Semantic Similarity** : 
   - Cela consiste à évaluer dans quelle mesure le sens de deux textes est similaire. On se concentre sur la signification des mots et des phrases, plutôt que sur leur forme exacte.
   - Exemple : "Le chat dort sur le tapis." et "Le félin se repose sur la moquette." sont sémantiquement similaires car ils ont des significations très proches, même si les mots utilisés sont différents.

2. **Token Level Syntactical Similarity** : 
   - Cela consiste à comparer les mots individuels (tokens) et leur ordre exact dans les phrases. C'est une approche plus orientée sur la forme des phrases.
   - Exemple : "Le chat dort sur le tapis." et "Le chat repose sur le tapis." sont syntactiquement similaires car la plupart des mots sont les mêmes et dans le même ordre.

### BERTScore

BERTScore utilise la **similarité sémantique** pour comparer des textes. Voici comment cela fonctionne :

1. **Encodage avec BERT** : 
   - Chaque texte est encodé en utilisant un modèle BERT pré-entraîné. BERT transforme les mots en vecteurs denses (embeddings) qui capturent des aspects sémantiques des mots dans leur contexte.

2. **Alignement des Tokens** : 
   - Les tokens de la phrase de référence et de la phrase candidate sont alignés de manière à maximiser la similarité cosinus entre leurs embeddings.
   - Cela signifie que même si les mots exacts diffèrent, les mots avec des significations similaires (comme "chat" et "félin") auront des vecteurs proches et contribueront à un score élevé.

3. **Calcul des Scores de Similarité** : 
   - Pour chaque token dans la phrase candidate, on trouve le token le plus similaire dans la phrase de référence en utilisant la similarité cosinus des embeddings.
   - On calcule des scores de précision, de rappel et de F1-score basés sur ces similarités cosinus.

### Exemple Illustratif

Supposons que nous comparions les phrases suivantes :

- Phrase de référence : "Le chat dort sur le tapis."
- Phrase candidate : "Le félin se repose sur la moquette."

**Étapes avec BERTScore :**

1. **Encodage** :
   - "Le chat dort sur le tapis." → vecteurs BERT : [v1, v2, v3, v4, v5]
   - "Le félin se repose sur la moquette." → vecteurs BERT : [u1, u2, u3, u4, u5]

2. **Alignement** :
   - On cherche pour chaque vecteur (u_i) (de la phrase candidate) le vecteur \( v_j \) (de la phrase de référence) le plus similaire (cosinus).
   - Par exemple, les vecteurs correspondant à "chat" et "félin" seront probablement très proches, et de même pour "dort" et "repose", "tapis" et "moquette".

3. **Calcul des Scores** :
   - **Précision** : Moyenne des similarités cosinus pour chaque token de la phrase candidate par rapport à la phrase de référence.
   - **Rappel** : Moyenne des similarités cosinus pour chaque token de la phrase de référence par rapport à la phrase candidate.
   - **F1-score** : Combinaison de la précision et du rappel pour obtenir un score global.

### Conclusion

BERTScore se concentre sur la **similarité sémantique** entre les phrases, en utilisant les représentations contextuelles riches fournies par BERT. Cela permet de capturer des nuances de sens même lorsque les mots exacts et leur ordre diffèrent, ce qui le distingue des méthodes purement syntaxiques basées sur les tokens.

meilleur resultat si pour rouge WE on utilise la même méthode que bert