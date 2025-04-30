# Windows_Lock_Screen_Image_Recorder

Log History
Version 1 : 
- initiale relase sans fonction avec dossiers absolus 'en dur'

Version 2 :
- nettoyage et optimisation de code avec gestion d'erreur
- creation de fonction
- creation d'un fichier config.ini
- utilisation de la variable %USERPROFILE%
- Ajout de l'historique dans le fichier config

Prochaines étapes : 
- enregistre le path dans le fichier init et entrer un boolean stipulant que l'exploration n'est plus à faire 
- améliorer la gestion d'erreur
- générer une erreur si le dossier origine n'existe pas ( pour x raison)
    - OPTION : si l'utilisateur rentre le dossier origine, le formater et le rentrer dans le fichier init   
- créer un exécutable python sur une machine où python n'est pas installé
- parcourir les utilisateurs et utiliser le premier pour lequel le  dossier origine existe
- OPTION : 
    avoir une interface utilisateur montrant les images (type carroussel)
    pouvoir choisir celles que l'on veut garder / supprimer
    MIEUX: changer les noms des images avec ce qu'elles représentent
