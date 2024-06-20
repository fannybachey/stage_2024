
# Pour la documentation 

## Summary Content Unit (SCU) de pyramide : 
1. Il est nécessaire d'identifier les phrases similaires dans le résumé. (Lettre et numéro : lettre pour le résumé et nombre pour la position de la phrase dans le résumé)
2. On essaye ensuite d'identifier plus précisément ce que contiennent les phrases pécédentes.
3. Procéder à l'annotation : 
- Attribuez à chaque SCU un indice unique, un poids et une étiquette en langage naturel
- À  quoi sert l'étiquette ? (- Elle libère le processus d'annotation de la dépendance à un langage de représentation sémantique.Elle oblige l'annotateur à être conscient d'un sens spécifique partagé par tous les contributeurs. Elle sert de rappel du sens complet dans le contexte, car les contributeurs à un SCU sont extraits de leur contexte.)
- Partition des SCUs en pyramide -> ça c'est automatique ? 

### Documentation pour le Processus d'Annotation Pyramid

#### Objectif
L'annotation pyramid vise à identifier et à organiser les unités de contenu de résumé (SCUs) afin de comparer les résumés produits par différents annotateurs.

#### Étapes du Processus

1. **Identification des Phrases Similaires**
   - **But**: Repérer les phrases ayant un contenu similaire dans différents résumés.
   - **Méthode**: Chaque phrase est indexée selon le résumé (A, B, C, etc.) et sa position dans celui-ci (1, 2, 3, etc.).
   - **Exemple**:
     ```
     A1 En 1998, deux Libyens inculpés en 1991 pour l'attentat de Lockerbie étaient toujours en Libye.
     B1 Deux Libyens ont été inculpés en 1991 pour avoir fait exploser un jumbo jet de la Pan Am au-dessus de Lockerbie, en Écosse, en 1988.
     C1 Deux Libyens, accusés par les États-Unis et la Grande-Bretagne d'avoir bombardé un avion de la Pan Am à destination de New York au-dessus de Lockerbie, en Écosse, en 1988, tuant 270 personnes, ont été hébergés pendant 10 ans par la Libye, qui prétendait que les suspects ne pouvaient pas obtenir un procès équitable en Amérique ou en Grande-Bretagne.
     D2 Deux suspects libyens ont été inculpés en 1991.
     ```

2. **Inspection Fine pour Sous-Parties**
   - **But**: Identifier les sous-parties spécifiques et leurs similarités plus fines entre les phrases.
   - **Méthode**: Décomposer les phrases en segments plus petits et les regrouper en SCUs.
   - **Exemple**:
     ```
     SCU1 (w=4) : deux Libyens ont été officiellement accusés de l'attentat de Lockerbie
     A1 [deux Libyens]1 [inculpés]1
     B1 [Deux Libyens ont été inculpés]1
     C1 [Deux Libyens,]1 [accusés]1
     D2 [Deux suspects libyens ont été inculpés]1

     SCU2 (w=3) : l'inculpation des deux suspects de Lockerbie a eu lieu en 1991
     A1 [en 1991]2
     B1 [en 1991]2
     D2 [en 1991.]2
     ```

3. **Annotation des SCUs**
   - **But**: Attribuer un indice, un poids, et une étiquette descriptive à chaque SCU.
   - **Exemple**:
     ```
     SCU1 (w=4) : deux Libyens ont été officiellement accusés de l'attentat de Lockerbie
     SCU2 (w=3) : l'inculpation des deux suspects de Lockerbie a eu lieu en 1991
     ```

4. **Partition des SCUs en Pyramide**
   - **But**: Organiser les SCUs par niveau de poids, du plus élevé au plus bas.
   - **Méthode**: Les SCUs de poids 4 sont au sommet, ceux de poids 3 juste en dessous, etc.
   - **Exemple**:
     ```
     Niveau 1: SCUs de poids 4
     SCU1 : deux Libyens ont été officiellement accusés de l'attentat de Lockerbie

     Niveau 2: SCUs de poids 3
     SCU2 : l'inculpation des deux suspects de Lockerbie a eu lieu en 1991
     ```

5. **Calcul du Score de Contenu Optimal**
   - **Formule**: 
     ```
     Max = ∑(i=j+1, n) i× |Ti| + j × (X − ∑(i=j+1, n) |Ti|)
     ```
   - **But**: Déterminer le score pyramidal pour un résumé donné.

6. **Vérification de la Fiabilité et Robustesse**
   - **But**: Assurer la cohérence et la fiabilité des annotations avec une formation minimale.

### Exemple Complet
Prenons un corpus de résumés contenant les phrases suivantes :

```
Résumé A:
A1 En 1998, deux Libyens inculpés en 1991 pour l'attentat de Lockerbie étaient toujours en Libye.

Résumé B:
B1 Deux Libyens ont été inculpés en 1991 pour avoir fait exploser un jumbo jet de la Pan Am au-dessus de Lockerbie, en Écosse, en 1988.

Résumé C:
C1 Deux Libyens, accusés par les États-Unis et la Grande-Bretagne d'avoir bombardé un avion de la Pan Am à destination de New York au-dessus de Lockerbie, en Écosse, en 1988, tuant 270 personnes, ont été hébergés pendant 10 ans par la Libye, qui prétendait que les suspects ne pouvaient pas obtenir un procès équitable en Amérique ou en Grande-Bretagne.

Résumé D:
D2 Deux suspects libyens ont été inculpés en 1991.
```

- **Étape 1** : Identifiez les phrases similaires.
- **Étape 2** : Inspectez les phrases pour trouver les sous-parties similaires.
- **Étape 3** : Annotez les SCUs.
- **Étape 4** : Classez les SCUs en niveaux pyramidaux.
- **Étape 5** : Calculez le score de contenu optimal.
- **Étape 6** : Assurez la fiabilité de l'annotation.

Cette documentation vise à fournir une compréhension claire et concise du processus d'annotation pyramid.


### Documentation pour l'Extraction et l'Annotation avec les Triplets RDF

#### Objectif
Utiliser des triplets RDF (Resource Description Framework) pour formaliser les unités de contenu des résumés et ainsi faciliter leur comparaison et leur analyse.

#### Étapes du Processus

1. **Identification des Phrases Similaires**
   - **But**: Repérer les phrases ayant un contenu similaire dans différents résumés.
   - **Méthode**: Chaque phrase est indexée selon le résumé (A, B, C, etc.) et sa position dans celui-ci (1, 2, 3, etc.).
   - **Exemple**:
     ```
     A1 En 1998, deux Libyens inculpés en 1991 pour l'attentat de Lockerbie étaient toujours en Libye.
     B1 Deux Libyens ont été inculpés en 1991 pour avoir fait exploser un jumbo jet de la Pan Am au-dessus de Lockerbie, en Écosse, en 1988.
     C1 Deux Libyens, accusés par les États-Unis et la Grande-Bretagne d'avoir bombardé un avion de la Pan Am à destination de New York au-dessus de Lockerbie, en Écosse, en 1988, tuant 270 personnes, ont été hébergés pendant 10 ans par la Libye, qui prétendait que les suspects ne pouvaient pas obtenir un procès équitable en Amérique ou en Grande-Bretagne.
     D2 Deux suspects libyens ont été inculpés en 1991.
     ```

2. **Extraction des Triplets RDF**
   - **But**: Transformer chaque phrase en triplets RDF sous la forme `(sujet, prédicat, objet)`.
   - **Méthode**: Identifier les sujets, prédicats et objets dans chaque phrase.
   - **Exemple**:
     ```
     A1: (Deux Libyens, inculpés, en 1991 pour l'attentat de Lockerbie)
     B1: (Deux Libyens, ont été inculpés, en 1991 pour avoir fait exploser un jumbo jet de la Pan Am)
     C1: (Deux Libyens, accusés, par les États-Unis et la Grande-Bretagne d'avoir bombardé un avion de la Pan Am)
     D2: (Deux suspects libyens, ont été inculpés, en 1991)
     ```

3. **Annotation des Triplets RDF**
   - **But**: Attribuer une étiquette descriptive et une relation contextuelle à chaque triplet RDF.
   - **Exemple**:
     ```
     (Deux Libyens, inculpés, en 1991 pour l'attentat de Lockerbie) -> inculpation en 1991
     (Deux Libyens, ont été inculpés, en 1991 pour avoir fait exploser un jumbo jet de la Pan Am) -> inculpation en 1991, explosion de jumbo jet
     (Deux Libyens, accusés, par les États-Unis et la Grande-Bretagne d'avoir bombardé un avion de la Pan Am) -> accusation par les États-Unis et la Grande-Bretagne, bombardement d'un avion
     (Deux suspects libyens, ont été inculpés, en 1991) -> inculpation en 1991
     ```

4. **Consolidation des Triplets RDF**
   - **But**: Regrouper les triplets similaires pour former une représentation unifiée de l'information.
   - **Méthode**: Comparer les étiquettes et les relations contextuelles pour fusionner les triplets similaires.
   - **Exemple**:
     ```
     Triplet consolidé 1: (Deux Libyens, inculpés, en 1991 pour l'attentat de Lockerbie)
     Triplet consolidé 2: (Deux Libyens, ont été inculpés, en 1991 pour avoir fait exploser un jumbo jet de la Pan Am)
     Triplet consolidé 3: (Deux Libyens, accusés, par les États-Unis et la Grande-Bretagne d'avoir bombardé un avion de la Pan Am)
     ```

5. **Vérification de la Cohérence et de la Précision**
   - **But**: S'assurer que les triplets RDF sont cohérents et représentatifs des informations originales.
   - **Méthode**: Réviser manuellement les triplets pour corriger les incohérences ou les erreurs.
   - **Exemple**:
     ```
     (Deux Libyens, inculpés, en 1991 pour l'attentat de Lockerbie) -> validé
     (Deux Libyens, ont été inculpés, en 1991 pour avoir fait exploser un jumbo jet de la Pan Am) -> validé
     (Deux Libyens, accusés, par les États-Unis et la Grande-Bretagne d'avoir bombardé un avion de la Pan Am) -> validé
     ```

### Exemple Complet
Prenons un corpus de résumés contenant les phrases suivantes :

```
Résumé A:
A1 En 1998, deux Libyens inculpés en 1991 pour l'attentat de Lockerbie étaient toujours en Libye.

Résumé B:
B1 Deux Libyens ont été inculpés en 1991 pour avoir fait exploser un jumbo jet de la Pan Am au-dessus de Lockerbie, en Écosse, en 1988.

Résumé C:
C1 Deux Libyens, accusés par les États-Unis et la Grande-Bretagne d'avoir bombardé un avion de la Pan Am à destination de New York au-dessus de Lockerbie, en Écosse, en 1988, tuant 270 personnes, ont été hébergés pendant 10 ans par la Libye, qui prétendait que les suspects ne pouvaient pas obtenir un procès équitable en Amérique ou en Grande-Bretagne.

Résumé D:
D2 Deux suspects libyens ont été inculpés en 1991.
```

- **Étape 1** : Identifiez les phrases similaires.
- **Étape 2** : Transformez les phrases en triplets RDF.
- **Étape 3** : Annotez les triplets avec des étiquettes descriptives.
- **Étape 4** : Consolidez les triplets similaires.
- **Étape 5** : Vérifiez la cohérence et la précision des triplets RDF.

### Conclusion
Cette documentation fournit une méthode structurée pour utiliser les triplets RDF dans l'extraction et l'annotation des unités de contenu de résumé, permettant une analyse et une comparaison plus précises des résumés.