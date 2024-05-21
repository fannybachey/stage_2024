### Les différents outils d'évaluation 
= Un package + son évaluation (ce qui n'avait pas été proposé par les précédents)
Méthodes automatiques d'évaluation qui mesurent la similarité entre 2 résumés. 

Plusieurs variantes mais l'idée principales est d'assigner un score à un résumé par rapport à un ou plusieurs résumés de références. 

1. ROUGE N = n-gram Co-occurence Statisitics 
Compare les n-gram d'un résumé candidat à un résumé de référence.
EX : rouge-1 = unigram 
On peut changer la granularité => rouge-2 et on travail avec des bi-grams 
À chaque fois qu'il y a de nouvelles références, le dénominateur augmente donc permet d'avoir plus de variété dans les formulations. 
Mais dans le cas où il existe plusieurs références ? 
-  On fonctionne toujours avec des pairs, ensuite question pour l'évaluation avec multi-référence. Demander confirmation. 

2. ROUGE L = Longest common sub-sequence
Considère chaque résumé comme une séquence de mot et cherche la sous-séquence consécutive identique la plus longue entre les 2 résumés. Capture la structure de la phrase avec plus de précision.
Différence entre RougeL et RougeLsum = Lsum est une métrique que l'on calcule sur l'ensemble d'un résumé et rougeL = une moyenne sur des phrases individuelles. 
Les différences clés : 
- ROUGE-L ignores newlines and computes the LCS for the entire text. This is appropriate when the candidate and reference summaries contain a single long sequence.
- ROUGE-L*_sum_* splits the text into sentences based on newlines and computes the LCS for each pair of sentences. It then takes the union of all LCS scores. This is appropriate when the candidate and reference summaries contain multiple sentences.
- ROUGE-L tends to give higher scores when the summaries contain similar content, regardless of sentence structure.
- ROUGE-Lsum penalizes differences in sentence structure more since it computes the LCS for each pair of sentences.

3. ROUGE W 
Rouge-L auquel on ajoute le "rappel" de la taille de "the lenght of consecutive matches encountered so far to a regular two dimensional dynamic program table computing LCS"
k indique la taille de les actuels matchs consécutifs.

5. ROUGE S 
 Permet de rechercher des mots consécutifs du texte de référence qui apparaissent dans la sortie du modèle mais qui sont séparés par un ou plusieurs autres mots.
 \+ Rouge-SU qui permet d'ajouter à rouge-s le calcul des unigram comme des unités
### Évaluation de ces méthodes 
#### Résultats 
Pour évaluer leur méthode, ils calculent la corrélation entre les scores ROUGE assignés aux résumés et le score assigné au résumé par des humains. 
Utilisation de la corrélation de Pearson (et 2 autres mais comme les résultats se rejoignent ils ne sont pas dans l'article)
Assez bon résultat, pour toutes les métriques (sauf certaines mais logique) 
5 points qu'ils ont relevé : 
- (1) ROUGE-2, ROUGE-L, ROUGE-W, and ROUGE-S worked well in single document summarization tasks, 
- (2) ROUGE-1, ROUGE-L, ROUGE-W, ROUGE-SU4, and ROUGE-SU9 performed great in
evaluating very short summaries (or headline-likesummaries), 
- (3) correlation of high 90% was hard to achieve for multi-document summarization tasks but ROUGE-1, ROUGE-2, ROUGE-S4, ROUGE-S9, ROUGE-SU4, and ROUGE-SU9 worked reasonably well when stopwords were excluded from matching,
- (4) exclusion of stopwords usually improved correlation, and 
- (5) correlations to human judgments were increased by using multiple references.

#### Critiques
On peut se demander si on peut vraiment utiliser cette mesure de corrélation, est-ce que les données respectes vraiment les conditions nécessaires pour la bonne application de Pearson.
Comparaison se fait par rapport à une évaluation manuelle des corpus mais est-ce que c'est vraiment une note pertinente pour évaluer les résumés, surtout qu'il n'y a qu'une seule note de référence. 
On peut aussi s'interroger sur le fait que les tests ne sont effectués que sur DUC (3 années donc c'est pas mal mais quand même)
