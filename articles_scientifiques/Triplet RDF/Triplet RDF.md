Sources : 
https://pageperso.lis-lab.fr/bernard.espinasse/wp-content/uploads/2021/12/2-Cours-RDF-BE-4P.pdf
___ 

## Sémantiques des Données 

normes W3C
Aider les machines à décoder le langage humain 
RDF -> Ressource Description framework 
Attacher à une ressource un ensemble de métadonnées cad des propriétés qui la caractérise au mieux et les partager 

RDF propose 2 choses : 
- un modèle de données standardisé
- des formats d'échange de données (C'est ici que l'on parle de triplet)

Puisque les phrases humaines sont des  données complexes, il est nécessaire e les simplifier pour en faire plusieurs faits simples interprétable par la machine. 
Sujet - prédicat - objet 
relation établit entre un sujet et son prédicat. 

Ce sont ces petites phrases déclaratives que l'on nomme triplet RDF. 
constituer toujours des mêmes 3 éléments. 
- Exprime un fait 
- chaque élément est appelé ressource
- correspond au cadre de la ressource-> RDF : ressource description framework, modèle et échange de données 
- Structure atomique = ne peut être réduit ou décomposé. 

chaque élément possède une IRI ( International Ressource Identifier)
Utiliser pour décrire les ressources, permet d'élargir les caractères pris en compte dans les adresses (= adresses étendues). Cette IRI peut-être typée. 
Possible de les représenter sous forme de graphe. 

### Graphe RDF 

- Exemple de Graphe ou collection de Triplets = c'est si le sujet possède plusieurs objets et donc plusieurs prédicats. 
Représentation : 2 noeuds reliés par un arc, arc représente le prédicat 
