
**1. Contexte et définition du problème**
	 *Exposer en quelques mots les fondements de la demande* 
    
 - Création d'un logiciel pour l'aide à l'évaluation de résumés générés automatiquement. 
- Il est nécessaire de créer une interface qui permet à l'utilisateur de visualiser les différents résumés générés et ceux de références en parallèle du document source. 
- ainsi que les résultats (éléments ?) générés par les différentes métriques d'évaluation (ROUGE, pyramid, JS(...))
 
- **1.2 Objectifs**
	*Exprimer le niveau des attentes et les résultats attendus* 

- Facilité une évaluation semi-automatique 
- améliorer la précision de l'évaluation, automatiser certaines tâches (par exemple la reconnaissance des unité de sens avec automated pyramid)
- permettre de corriger les résumés 

### 2. Principes généraux/ aspects fonctionnels

- **2.1 Fonctionnalités principales**
    - Description détaillée des fonctionnalités principales du logiciel
        - Importation de résumés à évaluer
        - Comparaison de résumés avec des résumés de référence
        - Utilisation de métriques d'évaluation comme ROUGE, BLEU, etc.
        - Annotations attractives (comme summvis), souligner, surligner, mettre en gras... 

### 3. Aspects fonctionnels 

- **3.1 Utilisateurs et rôles**
    - annotateur ?
    - Même permission pour tout le monde ? 

- **3.2 Scénarios d'utilisation**
    - On importe dans le logiciel un peu à la façon de TXM le corpus que l'on veut annoter, préciser le format ? Possibilité d'ajouter un texte qui peut-être depuis l'interface résumé par différents modèles.
     - on importe un le document source et 1 ou plusieurs résumés, on propose à l'utilisateur une visualisation qui lui permet de juger de la qualité d'un résumé et on lui permet de 

- **3.3 Interface utilisateur**
    - Clarté ? Il faut une interface interactive qui permet à l'utilisateur de facilement voir les similarités entre les résumés, en soulignant, surlignant le texte, etc... 
    - Inspiration de summvis, interface comme ci-dessous : 
![[Pasted image 20240610130806.png]]


- **3.4 Métriques d'évaluation**
    - Liste et description des métriques d'évaluation utilisées :
	    - ROUGE (à voir quelles métriques on décide d'implémenter)
	    - Pyramid (automated bien sûr mais peut-être de la doc sur normal ?)
	    - Scores statistiques ? Peut-être dans l'esprit de donner une note plus globale sur les résumés. 
	    - Score BERT ...
	    - autres  ??? 

    - Comment et quand ces métriques seront appliquées : 
		- Une fois que le document est mis dans le logiciel, il faut que le traitement se fasse pour chaque pair (est-ce qu'on propose le même format que sur summvis avec la comparaison entre source document/résumé et résumés/résumé de référence. )


## Description formelle des besoins 
-> Décrire son besoin en terme de fonctionnalités

*Exemple :* 

**Fonction principale** : Gestion des résumés candidats
Sous-fonctions :  
- importer un nouveau résumé 
- corriger/modifier un résumé existant 
- supprimé un résumé candidat  
Pour chaque fonction  = un tableau sous cette forme : 
![[Pasted image 20240618124444.png]]u
source : https://www.manager-go.com/gestion-de-projet/dossiers-methodes/elaborer-un-cdc


2 méthodes : (mais on en retient qu'une seule)

- 1 : aide annotation, pour faire le gold standard; aider l'annotateur à extraire l'information avec extraction de connaissance
=> MAIS ce n'est pas dans cette direction que l'on va aller parce que ça n'est pas forcément facile à mettre en place techniquement 

- 2 : On ne cherche pas à proposer de l'annotation automatique, mais on permet à l'utilisateur de rentrer les documents dans le logiciel. Ça n'est pas le plus coûteux d'annoter mais plutôt d'évaluer les dizaines de documents 
- Ajouter les méthodes d'annotation, SCU ? Triplet RDF (en tant qu'élément unique de l'informatique) ? Il faut définir ce que je veux utiliser, est-ce que je propose à l'utilisateur de choisir ? 

Il faut renseigner les infos à l'utilisateur, que ça soit la DOCUMENTATION ou lui permettre d'avoir accès à de l'info partout tout le temps, surtout pour l'annotation. 

C'est mon rôle de proposer les guidelines -> je dois aussi donner des exemples et faire en sorte que ça soit le plus accessible possible. 
Facile normalement d'ajouter de l'info car ils sont sur Angular 
[[Angular]]

Se pose aussi la question de l'annotation concurrente, quel est le processus à suivre pour avoir une bonne concurrence entre les annotations. 
Comment bien annoter ? 
On vise une bonne co-annotation, intéressant de regarder ce que c'est bien annoter => on peut approfondir cette question Karen Fort 

On cherche le CONSENSUS, comment on arrive à ce consensus ? 
2 façons qui peuvent être envisager : 
- Super-user 
- Discussion 
Le mieux ça serait d'avoir les 2, à voir au niveau de la difficulté que ça apporte au projet. 

Plus généralement c'est à moi de mettre le cadre théorique

Technique -> aussi la question de la proposition automatique que l'on propose notamment dans la façon d'aider l'annotateur en mettant en évidence ce qui est susceptible de ressembler à l'unité d'information dans les phrases et qui correspondent probablement au sens. 

Si possible ça peut aussi être intéressant d'apporter de l'information sur la contradiction. 
Est-ce que l'on retrouve des contre-sens entre les résumés ? Est-ce qu'ils sont pénalisés ? 
Exemple bon score avec ROUGE mais contre sens qui n'aura aucun impact sur le score final que l'on donne à l'évaluation. 
Mais après ça n'est pas la priorité, on le garde dans un coin si jamais c'était possible d'ajouter une fonctionnalité qui permet de le prendre en compte.

Il faut aussi se poser la question de la répartition des différents résumés à annoter par les annotateurs. 
Une fois que le corpus est renseigné, comment on fait pour distribuer les résumés aux annotateurs ? Combien d'annotateurs par résumé ? 
On peut utiliser un randoms mais il faut aussi poser des contraintes (avoir en vision la qualité algorithmique de ce problème)
cb de résumés par utilisateurs ? 
Il faut qu'il y ait un partage, que ça "tourne"
C'est à moi de décider et de définir comment ils seront dispatchés

Mais donc il faut voir comment faire quand les contraintes ne sont pas parfaitement réalisable. Ex : si je dis 10 résumés par annotateur mais que j'ai seulement 10 annotateurs et 120 résumés, comment je dois faire ? 

Voir aussi ce qui concerne le résumé de référence pour la cohérence de l'annotation. 


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