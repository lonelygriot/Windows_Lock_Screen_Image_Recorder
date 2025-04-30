import os
from datetime import datetime
from shutil import copy
from PIL import Image
from configparser import ConfigParser


"""
Log History
Version 1 : 
- initiale relase sans fonction avec dossiers absolus 'en dur'

Version 2 :
- nettoyage et optimisation de code avec gestion d'erreur
- creation de fonction
- creation d'un fichier config.ini
- utilisation de la variable %USERPROFILE%
- Ajout de l'historique dans le fichier config

prochaines étapes : 

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

"""

#pour évaluer la taille des fichiers il faut d'abord les mettre en .jpg
# copier les images > 100ko qui sont dans Assets et les mettre dans le dossier Fonds ecran

#explorer le dossier et copie/colle chaque fichier > 100ko 
# fonction exploration
# fonction comparaison taille fichier 

# def gestion_erreur(dossier):
#     if not os.path.exists(dossier):
#         os.makedirs(dossier)
#         print("New folder created for : "+ dossier)


def creation_dossier_utilisateur(dossier_fichier_ini):
    dossier= os.path.join(os.environ['USERPROFILE'],str(dossier_fichier_ini))
    if not os.path.exists(dossier):
        os.makedirs(dossier)
        print("New folder created for : "+ dossier)
    return dossier


os.chdir(os.path.dirname(os.path.abspath(__file__)))

fichier=ConfigParser()
fichier.read('config.ini')
chemin=fichier['Chemin_fichier']


dossier_origine=     creation_dossier_utilisateur(chemin['original'])
dossier_temporaire=  creation_dossier_utilisateur(chemin['dossier_temporaire'])
dossier_destination= creation_dossier_utilisateur(chemin['dossier_destination'])


#copie dans le repertoire de travail
cwd=os.chdir(dossier_origine)
for file in os.listdir(dossier_origine):
    copy(file,dossier_temporaire)

cwd=os.chdir(dossier_temporaire)
  
for file_temp in os.listdir(cwd):
    img=Image.open(file_temp)
    #print(img.size[0])
    if img.size[0]<1920:
        img.close()
        os.remove(file_temp)

    else:
        img.close()
        try:    
            os.rename(file_temp,file_temp+".jpg")
        except FileExistsError:
            print('doublon fichier jpg')
            
a=0            

" on copie et on retire les fichiers temporaires restants"
for file_temp in os.listdir(cwd):
    copy(file_temp,dossier_destination)
    os.remove(file_temp)

cwd=os.chdir(dossier_destination)

for final_file in os.listdir(cwd):
    creation_date = os.path.getctime(final_file)
    date_fichier = datetime.fromtimestamp(creation_date)
    #date du jour
    today_date = datetime.today()

    if( today_date.year == date_fichier.year and 
        today_date.month == date_fichier.month and  
        today_date.day == date_fichier.day):
        a+=1 
        
print("le nombre de fichiers créés est de : "+str(a))


os.chdir(os.path.dirname(os.path.abspath(__file__)))
fichier_log=ConfigParser()
fichier_log.read('history.txt')
log=fichier_log['Historique']


date_jour= str(today_date.year)+'_'+ str(today_date.month)+'_'+str(today_date.day)
log[date_jour] = str(a)
with open('history.txt','w') as aujourdhui :
    fichier_log.write(aujourdhui)
