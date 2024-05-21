from rouge_score import rouge_scorer

# Script qui permet de calculer les scores des différentes métriques de rouge. 
# Script à exécuter avec l'environnement "stage"

# Il faut vérifier si les données sont normaliser/traiter avant que la métrique ne soit utilisé. Et si on l'utilisait, quel était l'impact sur le score
# Nécessaire de le calculer sur des corpus plus volumineux. Peut-être les corpus de références. 

scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL','rougeLsum'], use_stemmer=True)
scores = scorer.score('The quick brown fox jumps over the lazy dog',
                      'The quick brown dog jumps on the log.')

print (scores)

''' 
Sortie : 

{'rouge1': Score(precision=0.75, recall=0.6666666666666666, fmeasure=0.7058823529411765), 
'rougeL': Score(precision=0.625, recall=0.5555555555555556, fmeasure=0.5882352941176471), 
'rougeLsum': Score(precision=0.625, recall=0.5555555555555556, fmeasure=0.5882352941176471)}

'''