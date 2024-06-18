
**1. Contexte**
    - Création d'un logiciel pour l'aide à l'évaluation de résumés générés automatiquement. 
    - Il est nécessaire de créer une interface qui permet à l'utilisateur de visualiser les différents résumés générés et ceux de références en parallèle du document source. 
     - ainsi que les résultats (éléments ?) générés par les différentes métriques d'évaluation (ROUGE, pyramid, JS(...))
 
- **1.2 Objectifs**
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


