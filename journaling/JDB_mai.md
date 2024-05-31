# STAGE MAI 2024 

=> Objectifs : dresser un premier états de l'art, lectures d'articles scientifiques et 2 présentations pour voir l'avancée. 
- 2 présentations d'articles 
- Se familiariser avec l'outil dans l'optique de rédiger un cahier des charges pour un projet étudiant. 


DATES IMPORTANTES : 
- **17 mai : première présentation** : présentation de 5 articles scientifiques dans le but de produire un état de l'art. 
- **30 mai : deuxième présentation** : avancer régulièrement dans la lecture des articles scientifiques !!!

___ 

## Du 6 au 16 mai : 
- Lecture des articles et préparation de la présentation

___ 
## Vendredi 17 mai 
Présentation de 5 articles scientifiques, support disponible. 
- Re-evaluation Evaluation in Text Summarization
- ROUGE : A package for Automatic Evaluation of Summaries 
- Better Summarization Evaluation with Word Embeddings for ROUGE 
- Evaluating Content Selection in Summarization : The Pyramid Method 
- Automated Pyramid Summarization Evaluation

_________
## Mardi 21 mai 

### Mise en place de l'environnement : 
- installation de git 
- création d'un github stage pour assurer le suivi et rassembler le travail effectué.
- utilisation des outils rouge, utilisation d'un git : https://github.com/google-research/google-research/tree/master/rouge

### ROUGE's computation 

Objectifs : test sur quelques phrases pour comprendre le fonctionnement et s'approprier les métriques. 
Scripts pour démonstration ROUGE-Lsum 
**rouge.py** 
Pour l'utiliser : environnement stage, pour l'activé depuis home : 

``` bash
$ source environments/stage/bin/activate
```

### Lecture

- Lecture : The limits of automatic summarisation according to ROUGE (à terminer demain) 

_________

## Mercredi 22 mai 

TO DO : 
- [ ] Demander les différents corpus 
- [x] Continuer la lecture des articles

- Lecture de "The limits of automatic summarisation according to ROUGE" de Natalie Schluter 
En + : théorie des graphes pour prouver que c'est un problème NP-hard + impossible d'avoir un score de 100% donc sous-entends que même les résumés humains ne sont pas forcément bons

- Début lecture de "Overview of the TAC 2008 Update Summarization Task"


____ 

## Jeudi 23 mai 

TO DO : 
- [x] Commencer le diapo pour la présentation (ROUGE et TAC)
- [ ] Envoyer un mail pour les corpus 
- [ ] Tester ROUGE sur un corpus TAC 


- Début de la présentation pour le 30
- Lecture article : "Overview of the TAC 2008 Update Summarization Task" (il reste à terminer le diapo)
Permet de voir les méthodes proposées par les candidats dans la création des résumés, donne un aperçu plus globale des différences que l'on retrouve dans les résultats d'évaluation des résumés manuels et ceux générés automatiquement. 

________________

## Vendredi 24 Mai

TO DO : 
- [ ] Envoyer un mail pour les corpus 
- [ ] Tester ROUGE sur un corpus TAC (ou DUC ?? vérifier)

- Téléchargement dataset cnn/dm (script : cnn_dm.py)
- lecture article : Automatically Evaluating Contenet Selection in Summarization without Human Models 

_______

## Lundi 27 Mai


_____
## Mardi 28 Mai 

- Envoie mail pour dataset (DUC 2004 ET DUC 2005)
- Lecture article et diapo ++


____ 
## Mercredi 29 Mai 

- Réception des datasets DUC 2004 et 2005 
- Demande DUC 2006 - DUC 2007

TO DO : 
- [x] Envoyer les demandes pour TAC 
- [x] Télécharger données en local pour CNN/DM 

___ 
## Jeudi 30 Mai 

- envoi de tous les mails restant pour les demandes de corpus 
- Lecture d'articles, présentation 

___ 

## Vendredi 31 Mai 

- Clone du git de summvis 
- Problèmes de compatibilités des dépendances dc pour l'instant impossible d'installer (à voir ce week-end pour essayer de l'installer sur appareil personnel)