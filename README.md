# Windows_Lock_Screen_Image_Recorder

## FEATURES

Ce code permet de sauvegarder les images présentées sur l'ecran d'accueil dans un dossier.  
Le dossier d'origine est l'endroit où Microsoft sauvegarde ces fichiers, il n'est pas à changer.  
Les deux autres dossiers sont des dossiers par défaut, personnalisable à l'envie.   
Le dossier transitoire '_temp' est utilisé pour opérer un certan nombre d'opération sur les fichiers, comme le filtrage et l'ajout d'une extension.  
Le dossier destination est l'endroit où seront finalement copié et comptés les images.  
Le fichier config.ini comprend les chemins relatifs vers les dossiers source/temporaire/destination.  
Le fichier history.txt implemente l'historique d'utilisation du code et le nombre de fichiers definitifs créés.  

***
Merci de m'envoyer vos commentaires ou vos suggestions d'améliorations ! 
***


## LOG HISTORY

**Version 1**  
- initiale relase sans fonction avec dossiers absolus 'en dur'

**Version 2**
- nettoyage et optimisation de code avec gestion d'erreur
- creation de fonction
- creation d'un fichier config.ini
- utilisation de la variable %USERPROFILE%
- Ajout de l'historique dans le fichier config

Prochaines étapes : 
- regarder dans history : si déjà executé à date, arreter
- regarder le dossier final : commparer les noms de fichiers présents : proposer de copie si absent , si OK copier, sinon suivant, si pas suivant , arreter , sinon ignorer  
- améliorer la gestion d'erreur
- générer une erreur si le dossier origine n'existe pas ( pour x raison)
    - OPTION : si l'utilisateur rentre le dossier origine, le formater et le rentrer dans le fichier init   
- créer un exécutable python sur une machine où python n'est pas installé
- parcourir les utilisateurs et utiliser le premier pour lequel le  dossier origine existe
- OPTION : 
    avoir une interface utilisateur montrant les images (type carroussel)
    pouvoir choisir celles que l'on veut garder / supprimer
    MIEUX: changer les noms des images avec ce qu'elles représentent

  Created by Benoit Logeay
  @2025 Windows Lock Screen Image Recorder
