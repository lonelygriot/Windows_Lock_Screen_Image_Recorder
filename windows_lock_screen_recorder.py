import os
from datetime import datetime
from shutil import copy
from PIL import Image
from configparser import ConfigParser

# returns the path made by USERPROFILE + config.ini path. 
# creates the folder if not existing
def creation_dossier_utilisateur(dossier_fichier_ini):
    dossier= os.path.join(os.environ['USERPROFILE'],str(dossier_fichier_ini))
    if not os.path.exists(dossier):
        os.makedirs(dossier)
        print("New folder created for : "+ dossier)
    return dossier

if __name__ == "__main__":
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    fichier=ConfigParser()
    fichier.read('config.ini')
    chemin=fichier['Chemin_fichier']

    dossier_origine=     creation_dossier_utilisateur(chemin['original'])
    dossier_temporaire=  creation_dossier_utilisateur(chemin['dossier_temporaire'])
    dossier_destination= creation_dossier_utilisateur(chemin['dossier_destination'])


    #copy of the files in the working directory
    cwd=os.chdir(dossier_origine)
    for file in os.listdir(dossier_origine):
        copy(file,dossier_temporaire)

    cwd=os.chdir(dossier_temporaire)

    # select the images with width = 1920, deletes other files
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

    # send the images to the destination folder
    for file_temp in os.listdir(cwd):
        copy(file_temp,dossier_destination)
        os.remove(file_temp)

    cwd=os.chdir(dossier_destination)

    # using creation dates,identify the exact number of added files
    # previously present images with same name not considered
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

    # add a new line in the history file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    fichier_log=ConfigParser()
    fichier_log.read('history.txt')
    log=fichier_log['Historique']


    date_jour= str(today_date.year)+'_'+ str(today_date.month)+'_'+str(today_date.day)
    log[date_jour] = str(a)
    with open('history.txt','w') as aujourdhui :
        fichier_log.write(aujourdhui)
