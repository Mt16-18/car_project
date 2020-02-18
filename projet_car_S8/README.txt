fichier à lire avant l'utilisation de l'exécutable match
------------------------------------------------------------------------

le programme match permet de prendre les coordonnées et l'angle (en temps réel) d'un objet portant 2 pastilles identifiables par template matching
(les fichiers doivent être au format png et ne pas dépasser la résolution de la caméra)

match permet aussi de trouver les coordonnées d'un autre objet (l'arrivée), aussi par template matching.


----------------------------------------
Comment l'utiliser

il faut dans le même répertoire que l'exécutable les fichiers images : template_avant.png, template_arriere.png et template_arrive.png
    Si une des images n'existe pas une capture image sera enregistrée à la place.

Les positions et angles seront enregistrer dans valeurs.txt
1- Position de la voiture
2-Position de l'arrivée
3-angle de la voiture en degrés par rapport à l'horizontal

----------------------------------
Arguments


Par défaut sans arguments 
