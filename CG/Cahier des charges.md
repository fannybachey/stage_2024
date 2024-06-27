

[[Documentation]]

**1. Contexte et définition du problème**
	 *Exposer en quelques mots les fondements de la demande* 
    
 - Création d'un logiciel pour l'aide à l'évaluation de résumés générés automatiquement. 
 - Permet une annotation en 2 phases : 
- Avec : 
	- une interface qui permet à l'utilisateur de visualiser les différents résumés générés à évaluer et ceux de références. 
- Résultats (éléments ?) générés par les différentes métriques d'évaluation (ROUGE, pyramid, JS(...))
- Ajout de propositions automatiques (pour faciliter le repérage des SCUs et/ou des triplets)
 
- **1.2 Objectifs**
	*Exprimer le niveau des attentes et les résultats attendus* 

- Facilité l'évaluation des résumés en facilitant le "repérage" des différentes unités de sens. 
- améliorer la précision de l'évaluation, *automatiser certaines tâches* (par exemple la reconnaissance des unité de sens avec automated pyramid)
- permettre de corriger les résumés 

### 2. Principes généraux/ aspects fonctionnels

- **2.1 Fonctionnalités principales**
    - Description détaillée des fonctionnalités principales du logiciel
        - Importation de résumés à évaluer
        - Comparaison visuel (afficher les 2 résumés) de résumés avec le résumé de référence ou le document source. 
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

