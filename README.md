This is the ESA applicant group project for Hackatown 2018 _ Red lights trafic control . 

## Inspiration
Victor a presque mis feu à la maison de Lucas, heureusement, les pompiers sont arrivés à temps. Mais que ce serait-il passé s'ils avaient été pris dans des embouteillages ? 

## What it does
Ce programme permet, à partir de la localisation du lieu de l'intervention, de choisir la caserne la plus proche, de déterminer le parcours à effectuer par les pompiers et de contrôler les feux de signalisation afin de faciliter leur trajet. Ce programme se limite à l'étude du quartier du Plateau de Montreal qui comporte 4 casernes et 194 feux. 

## How we built it
Les données utilisées, celle de l'emplacement des casernes et des feux de circulation sont celles fournies par _http://donnees.ville.montreal.qc.ca_ . Le programme a été implémenté en **python** puis en **JavaScript** afin d'utiliser une interface graphique issue de **Google-Maps**. 

## Challenges we ran into
Le principal défi a été l'utilisation de JavaScript car c'était une première pour tout le monde. 
La sélection des feux concernés a également pris un peu plus de temps que prévu: pour cela nous avons dû réutiliser des concepts de géométrie.

## Accomplishments that we're proud of
Nous sommes fières d'avoir pu présenter une interface _interactive_, _facile d'utilisation_ et _fonctionnelle_.

## What we learned
Nous avons appris à utiliser des données publiques pour les implémenter dans JavaScript.

## What's next for Feux Verts
Par la suite, il serait préférable d'étendre l'étude à tout Montreal. De plus, un algorithme de choix d'itinéraire optimum en fonction de la circulation en temps réel serait aussi à prévoir. 
