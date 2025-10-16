import requests
from bs4 import BeautifulSoup


print("On va faire une application qui vous envoie la date de naissance d'un acteur selon son nom depuis Wikipedia ..")
nom_acteur=input("Veuillez saisir le nom de l'acteur ici -->  ")

url=f'https://fr.wikipedia.org/wiki/{nom_acteur}'
result=requests.get(url)

page_content=BeautifulSoup(result.text,'html.parser')

#Une autre solution peut etre plus simple et efficace
body_finder=page_content.find('div',class_='mw-body-content')
other_finder=body_finder.find("div",class_='mw-content-ltr')
all_p=other_finder.find_all("p")

for p_items in all_p:
    txt=str(p_items.text)
    if (txt.find("né le")!=-1 or txt.find("née le")!=-1):
        ch=''
        position1=txt.find("né le")
        if position1==-1 :
            position1=txt.find("née le")
        nouv_txt=txt[position1+6:]
        liste_txt=nouv_txt.split()
        ch=liste_txt[0]+" "+liste_txt[1]+" "+liste_txt[2]
        break
    
    
date_naissance=ch
        
    
    


print(f"date naissance -->{date_naissance}")






