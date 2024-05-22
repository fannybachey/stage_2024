### Définition de base 
Pour un graphe  \( G = (V, E) ), où \( V \) représente les sommets et \( E \) les arêtes, un ensemble dominant est un sous-ensemble de sommets \( D \subseteq V \) tel que chaque sommet de \( V \) qui n'est pas dans \( D \) est adjacent à au moins un sommet de \( D \). En d'autres termes, chaque sommet qui n'est pas dans \( D \) doit avoir au moins un voisin dans \( D \). 
### Pondération et k-dominance
1. **Pondération** : Dans un graphe pondéré, chaque sommet \( v \in V \) a un poids associé, noté \( w(v) \). 
2. **k-dominance** : Un ensemble dominant k-pondéré est un ensemble \( D \subseteq V \) tel que la somme des poids des sommets dans \( D \) est maximale, et chaque sommet dans \( V \setminus D \) est adjacent à au moins un sommet dans \( D \). 
### Formulation du problème 

Le **max k-weighted dominating set problem** consiste à trouver un ensemble \( D \subseteq V \) de taille au plus k (où k est une constante donnée) tel que la somme des poids des sommets dans \( D \) soit maximale et que \( D \) soit un ensemble dominant. Cela signifie que l'ensemble \( D \) doit : 
1. Contenir au plus k sommets. 
2. Maximiser la somme des poids des sommets choisis. 
3. Assurer que chaque sommet qui n'est pas dans \( D \) est adjacent à au moins un sommet de \( D \). 
### Complexité 
Le problème est **NP-difficile** (NP-hard), ce qui signifie qu'il est au moins aussi difficile que les problèmes les plus difficiles de la classe NP. Aucune solution algorithmique en temps polynomial n'est connue pour ce problème, et il est peu probable qu'une telle solution existe (à moins que P=NP). 
### Réduction à l'extraction de résumé 
Dans le contexte de l'extraction de résumé mentionné dans votre extrait, le problème de trouver ==**un résumé extractif qui maximise la métrique ROUGE-1 peut être réduit au problème de l'ensemble dominant pondéré maximum à k.**== Cela montre que le problème d'optimisation de l'extraction de résumé est au moins aussi difficile que le max k-weighted dominating set problem, renforçant ainsi son statut de NP-difficile. 

### Conclusion 
En résumé, le problème du max k-weighted dominating set est ==un problème de théorie des graphes== où l'objectif est de sélectionner un sous-ensemble de sommets de taille au plus k, maximisant la somme des poids et assurant une couverture dominatrice sur le graphe. Ce problème est connu pour sa difficulté algorithmique, rendant ainsi l'optimisation des tâches similaires, comme l'extraction de résumé, également difficiles.

### Schéma pour le problème max k-weighted dominating set (voir feuille)
