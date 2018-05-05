# Projet - Chatbot

Ce programme est un chatbot en anglais qui possède 3 modes différents :

* mode 1 : Comme demandé dans le sujet, il s'agit d'un mode où le chatbot repond aux énoncés avec des backchannels.

* mode 2 : Comme demandé dans le sujet, le chatbot répond sous ce mode comme le chatbot Eliza.

* mode 3 : Pour ce mode "libre", nous avons choisi de faire un "Mean" bot.Notre idée était de créer un bot susceptible et fondamentalement méchant qui soit de plus en plus énervé.Le bot possède plusieurs niveaux d'humeur : Slightly annoyed, Pissed off, Angry, Does not respond et Quits.Parler au bot de certains sujets ou effectuer certaines actions énervent le bot qui engrange des "points d'humeur", passé un certain seuil, le bot monte d'un cran au niveau de l'humeur, rendant ainsi ses réponses plus aggressives. Passé le dernier niveau d'humeur, le bot quitte la conversation de lui-meme car il est trop énervé pour continuer.Il existe bien évidemment des moyens de calmer le bot, comme par exemple de lui exprimer des excuses ou de lui dire qu'on l'aime. Cela le fera redescendre un petit peu vers un niveau d'humeur plus calme.

## Prérequis

Aucune bibliothèque autre que celle de base n'a été utilisée pour notre projet. Il suffit d'avoir Python installé sur son ordinateur pour pouvoir l'exécuter.

## Exécution

Pour exécuter notre programme, il suffit d'entre la ligne de commande suivante :

```bash
/opt/anaconda3/bin/python main.py  [mode] [police]
```

```text
[mode] : entier qui vaut soit 1, 2 ou 3. Cela correspond au mode du chatbot que l'on souhaite utiliser.

[police] : entier qui vaut soit 0 soit 1. Cela correspond à la police que l'on souhaite utiliser pour la conversation (0 pour la police basique et 1 pour la police vaporwave).
```

## Exemples d'exécutions

Pour lancer le mode 1 en police vaporwave, on entre la commande suivante :

```bash
/opt/anaconda3/bin/python main.py 1 1
```

Pour lancer le mode 2 en police basique, on entre la commande suivante :

```bash
/opt/anaconda3/bin/python main.py 2 0
```

## Auteurs

Les personnes ayant contribué à ce projet sont :

* Morgan FEURTE (aka Drakyll sur GitHub)

* Jeffrey GONCALVES (aka JeffreyGoncalves sur GitHub)
