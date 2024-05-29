
(1) : Movement away from evaluation by correlation with human assessment
-> **Éloignement de la Corrélation avec l'Évaluation Humaine**: Les méthodologies d'évaluation des métriques de résumés se sont éloignées de la corrélation avec les jugements humains. 

(2) omission of important components of human assessment from evaluations . 
**Omission de Composants Importants**: Les évaluations actuelles omettent souvent des composants importants des jugements humains et incluent seulement une petite proportion des variantes possibles de la métrique ROUGE.

(3) absence of methods of significance testing improvements over a baseline. 
**Absence de Tests de Signification**: ils sont nécessaires pour évaluer les améliorations des métriques par rapport à une base de référence.


## 2. Related Work 

Méthodes qui sont basées sur la mesure de correlation avec un résumé humain.
-> Peut introduire des biais et favoriser les méthodes d'évaluation "recall-based". 
= introduit un biais en faveur des métriques basées sur le rappel.
Oublie également de certains autres aspects du résumés comme l'ordre des unités de résumés, scu ? 
	 
Formule du Rappel
Le rappel est calculé comme suit :

```
\[ \text{Rappel} = \frac{\text{Nombre de vrais positifs}}{\text{Nombre de vrais positifs + Nombre de faux négatifs}} \]

```

_____

## 3. Summarization Metric Evaluation 

1. Combining Quality and coverage 
-> on ajoute une note sur la qualité linguistique du résumé, en plus de mesurer le nombre d'unité qu'il couvre. 

Pour la première formule : 
- **Matching PUs (Processing Units)** : Il s'agit des unités de traitement (par exemple, des segments de texte) du résumé généré qui correspondent aux unités attendues dans le résumé de référence.
- **E** : Poids ou importance attribué aux unités de traitement correspondantes.
- **MUs (Model Units)** : Ce sont les unités de traitement totales présentes dans le résumé de référence.

**Interprétation:** Le Score de Couverture (CS) est calculé en prenant le nombre d'unités de traitement correspondantes (Matching PUs), en les multipliant par un facteur de poids (E), puis en divisant ce produit par le nombre total d'unités de traitement dans le résumé de référence (MUs). Cela donne une mesure de la couverture des éléments importants du résumé de référence par le résumé généré.
### Formule 2: Score d'Évaluation Humaine

Human Assessment Score=CS+MLQ2Human Assessment Score=2CS+MLQ​

**Définition des termes:**

- **CS** : Score de Couverture, tel que défini dans la première formule.
- **MLQ (Mean Linguistic Quality)** : Score moyen de qualité linguistique, qui est une évaluation subjective de la fluidité et de la lisibilité du texte généré.

**Interprétation:** Le Score d'Évaluation Humaine est la moyenne du Score de Couverture (CS) et du Score de Qualité Linguistique Moyenne (MLQ). Cela permet de combiner à la fois une évaluation objective (CS) et une évaluation subjective (MLQ) pour obtenir une mesure globale de la performance du résumé généré.

2. Rouge 
-> Rouge et ses métriques : en fonction des paramètres que l'on met, les résultats ne seront pas les mêmes. 
Le fait que ROUGE comprenne le score moyen ou médian des scores de résumés individuels permet l'application de méthodes standards de tests de significativité des différences dans les scores ROUGE au niveau du système, tandis que BLEU est limité à l'application de méthodes aléatoires."

3. Metric Evaluation by Pearson's r 
-> On évalue avec Pearson : mesure de la corrélation 

_____

## 4. Metric Significance Testing 






