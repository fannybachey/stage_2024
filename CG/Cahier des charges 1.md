
# INFORMATIONS RÉSUMÉS 


 - Création d'un logiciel pour l'aide à l'évaluation de résumés générés automatiquement. 
 - Permet une annotation en 2 phases : 
- Avec : 
	- pour la première phase : une interface avec document source et résumé de référence à annoter à plusieurs (entre 3 et 5 annotateurs)
	- une interface qui permet à l'utilisateur de visualiser les différents résumés générés à évaluer et ceux de références. 
- Ajout de propositions automatiques (pour faciliter le repérage des SCUs et/ou des triplets) pour la 2ème phase.

Il faut importer dans le logiciel un corpus composé des documents suivants : 
- un ensemble de texte 
- pour chaque texte un résumé de référence
- pour chaque texte, plusieurs résumé à évaluer 

## Exemple : 

- **Texte 1** : 
``` Friday , July 20 , 2007 Cristina Fernández de Kirchner Current senator and Argentine First Lady Cristina Fernandez de Kirchner announced her presidential candidacy yesterday evening in La Plata , a city 50 kilometers ( 31 miles ) away from Buenos Aires . Mrs. Kirchner announced her intention to run for president at the Argentine Theatre , the same location she used to start her 2005 campaign for the Senate as member of the Buenos Aires province delegation . A large security detail was in place at the theatre and eight city blocks were closed to traffic for the event . Outgoing Argentine president Néstor Kirchner , members of his office , and provincial governors were present at the ceremony . Julio Cobos , governor of Mendoza and possible campaign team member , was also there . Activists from Quebracho mobilized in La Plata to protest the candidacy of the First Lady , and created some disturbances near the event . None of the protesters was arrested , according to an official spokesman of La Plata Police Station . Recent polls indicate that Mrs. Kirchner has at least 40 percent voter support , which bodes well for winning on the first ballot in the upcoming October elections . According to Argentine newspaper La Nación , this speech signifies that the government is attempting to show solidarity in the midst of recent scandals : Felisa Miceli 's resignation to the Department of Economy after being accused of wrongdoing by a justice over the nearly $ 100,000 Argentine pesos and US$ 31,670 found in her office , and the alleged smuggling of weapons and irregularities in the office of the Secretary of Environment .```

- **Résumé de Référence**: "Argentina 's first lady to launch presidential bid"
- **Résumé à Évaluer** :
 
  - Résumé 1 : BART (CNNDM-trained)

	```Cristina Fernández de Kirchner announced her presidential candidacy yesterday evening in La Plata , a city 50 kilometers ( 31 miles ) away from Buenos Aires . A large security detail was in place at the theatre and eight city blocks were closed to traffic for the event.`

- Résumé 2 : BART (XSUM-trained)

	``` Cristina Fernandez de Kirchner has announced her intention to run for president of Argentina in October 's elections .```


____ 

## Annotation qui se fait en 2 phases : 

PHASE 1 : Annotation du résumé de référence 
Plusieurs annotateurs par résumé (entre 3 et 5), 1 résumé de référence par texte. 
Une fois que l'annotation est faîte, le responsable de corpus fait une vérification et règle les conflits 

PHASE 2 : Annotation de tous les résumés 
on récupère les résumés de référence de la première phase pour annoté tous les autres. C'est pendant cette phase que l'on ajoute les propositions automatique (WE) pour faciliter l'extraction des unités d'information. 


_____ 

## Unités d'information 

- Ce sont les tokens ou ensembles de tokens qui contiennent une information "atomique". Ce sont ces unités que l'on cherche à définir dans un premier temps dans les résumés de référence et que l'on cherche à identifier dans les résumés à évaluer. C'est une annotation pour évaluer le contenu. 

2 formes possibles : SCUs (pyramid) et triplet RDF 

SCU's: 
- SCU : « an SCU consists of a set of contributors that, in their sentential contexts, express the same semantic content. »
- 3 éléments : index, poids, label 

Triplet RDF : 
- toujours composé de 3 éléments -> Sujet - prédicat - objet 
- Exprime un fait 
- chaque élément est appelé ressource
- Structure atomique = ne peut être réduit ou décomposé. 

=> Il reste à trouver une méthode pour évaluer la qualité "littéraire" des résumés.



