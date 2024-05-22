# The limits of automatic summarisation according to ROUGE 

### Introduction 

- Perfect scores for extractive summarisation are theoretically computationally hard to achieve. 
=> théoriquement difficile d'obtenir des bons scores pour les résumés extractifs. 

- 100% perfect scores are impossible for higher quality datasets.
=> quasiment impossible d'obtenir un score de 100% 

- Relative perfect scores are highly diverse and unattainable by humans. 
=> Même avec le résumé de référence, on ne peut pas avoir un bon score, est-ce qu'on peut l'améliorer, on tend plutôt à dire que non. 

- State-of-the-art automatic summarisation is unsupervised. 
définition : exact algorithms are algorithms that always solve an optimization problem to optimality. 
Supervision permet-elle d'avoir une amélioration des systèmes ? (dans la consommation ?) 

NP-hardness : 
- difficulté de certains problèmes de calcul
1. **Classe NP** : NP (nondeterministic polynomial time) est une **classe de problèmes pour lesquels une solution peut être vérifiée rapidement, c'est-à-dire en temps polynomial.** Cela signifie qu'il existe un algorithme qui peut vérifier si une solution proposée est correcte en un temps raisonnable.
2. **Problèmes NP-complets** : Un problème est NP-complet s'il est à la fois dans NP et aussi "au moins aussi difficile" que n'importe quel autre problème dans NP. Autrement dit, si on pouvait résoudre un problème NP-complet rapidement (en temps polynomial), on pourrait résoudre tous les problèmes dans NP rapidement.
3. **NP-hard** : Un problème est NP-hard (NP-dur) s'il est "au moins aussi difficile" que les problèmes NP-complets, même si le problème lui-même n'est pas nécessairement dans NP (ce qui signifie que même vérifier une solution peut prendre plus que du temps polynomial). En d'autres termes, un problème NP-hard est aussi difficile que les problèmes les plus difficiles de NP.
### Preliminaries 

Rappel sur comment est calculé ROUGE-n(S) 
3 datasets : 
- DUC 2004
- judgment-summary pairs scraped from the European Court of Human Rights case-law website, HUDOC.3 The test set consists of 138 pairs.
- a comprehensive dump of English language Wikipedia articles.

### ROUGE optimisation for extraction 
2 théorèmes 

- Rouge-1 -> NP-hard 
- Rouge n -> NP-hard 
Qu'est-ce qui est compliqué ? 
C'est de maximiser les scores et donc d'avoir un modèle que l'on peut vraiment améliorer. Il font 2 preuves de cette complexité. Les deux expériences se base sur ROUGE-N. 
Qu'en est-il pour les autres modèles.

Expérience 1 : Pour maximiser le score de ROUGE-1, il faut maximiser le nombre de tokens que l'on retrouve dans les deux documents, dans la limite des tokens disponibles.
Le problème de l'ensemble dominant pondéré maximum à k (ou max k-weighted dominating set problem) est une variante complexe du problème de l'ensemble dominant en théorie des graphes. 
Voir : [[Ensemble dominant dans la théorie des graphes]]

#### Lien avec le max k-weighted dominating set problem 

1. On imagine que chaque token du document est un sommet dans un graphe, les sommets représentent la similarité ou la connexion entre les tokens.  
2. on pondère les sommets, chaque token à un poids =le nombre de fois qu'il apparaît dans le résumé de référence.
3. Ensemble dominant de token : on choisi un sous-ensemble de token de sorte à ce que ce sous-ensemble maximise le chevauchement des tokens. 

- Pour un graphe cubique G=(V,E)G=(V,E), chaque sommet vv a un poids 
wv=∣N(v)∪{v}∣=4wv​=∣N(v)∪{v}∣=4 (où N(v)N(v) est le voisinage de vv).
- La réduction consiste à transformer ce problème en un document DD où chaque phrase svsv​ représente N(v)∪{v}N(v)∪{v}.
- Le résumé extractif SS dans DD doit maximiser ROUGE-1, ce qui revient à maximiser le nombre de sommets adjacents dans le graphe d'origine.

==En termes de résumé, cela signifie choisir des phrases qui couvrent un maximum de tokens partagés avec le résumé de référence.==

