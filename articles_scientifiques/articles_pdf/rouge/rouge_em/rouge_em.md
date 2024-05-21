oblèmes de ROUGE que l'on essaye de corriger avec les WE 
- unsuitable for abstractive summarization (really ?) or summaries with substantial paraphrasing 
- ne permet pas de mesurer la lisibilité ou la  fluidité des résumés générés

=> Proposition pour pallier au premier problème qui a été soulever, on capte donc plus d'information sémantique.
"word embeddings refer to the mapping of words into a multi-dimensional vector space"
On ne se base plus sur les simililarités lexicales mais sur les similarités sémantiques. 
Il le font avec word2vec.
Le preoblème c'est des qu'on a des n-gram > 1, on ne sait pas vraimetn comment les compute, donc on prend des vecteurs uniques que l'on multiplie ensemble. 

Evaluation sur TAC ? Donc difficile de vraiment comparer genre pas terrible. On peut s'interroger sur la légitimité de cette comparaison. 
