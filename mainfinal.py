from db import *

#la date aujourd'hui 
import datetime
from datetime import date
j0=datetime.date.today()

#input des données du patient
#nom+prenom
nom=input("nom du patient:")
prenom=input("prénom du patient:")
#numéro portable
numero="0"
while (((len(numero))!=8) or (numero.isnumeric())==False):
    numero=input("numéro portable du patient:")
    print(numero)
# CIN
cin="0"
while (((len(cin))!=8) or (cin.isnumeric())==False):
    cin=input("cin du patient:")
    print(cin)
    
#insertion des données de patient dans db 

insertPatient(cin, nom, prenom, numero)

#type de sérum disponible
list_SAR=["equirab","gammarab"]
SAR=""
r={}
x= getSerum()
for i in x: 
    print(i)
r=i
SAR=r["type_serum"]
dose_id=r["numero_lot"]
print(SAR)
print(dose_id)

#la date aujourd'hui 
import datetime
from datetime import date
j0=datetime.date.today()
print("aujourd'hui est :",j0) ;

# import the datetime module
import datetime
# format
format = '%Y-%m-%d'

#etat de l'animal
etat=""
while etat not in ["observable","non observable"] :
    
    etat=input("ETAT DE L'ANIMAL(observable/non observable):")
print(etat) ;

#nombre de lésion
nombre=""
list_nombre=["unique","multiple"]
while nombre not in list_nombre :
    nombre=input("nombre de lésions(unique/multiple):")
print(nombre) ;

#profondeur de la lésion
profondeur=""
list_profondeur=["profonde","superficielle"]
while profondeur not in list_profondeur:
    profondeur=input("profondeur de la lésion(profonde/superficielle):")
print(profondeur) ;

#siège de la lésion
siège=""
list_siège=["main droite","main gauche","cou","tête","pied droit","pied gauche","OGE","centré"]
list_extrémité=["main droite","main gauche","cou","tête","pied droit","pied gauche","OGE"]
while siège not in list_siège:
    siège=input("le siège de la lésion est(main droite,main gauche,cou,tête,pied droit,pied gauche,OGE,centré):")
print(siège) ;

#poid du patient
poid=0
poid=int(input("donner le poid du patient(veuillez saisir un entier):"))
print(poid,"kg")

#get from vaccin
v={}
x= getVaccins()
for i in x: 
    print(i)
v=i
    
#les conditions de vaccination

dose=0
if etat=="observable":
    if (profondeur=="superficielle" and(nombre=="unique") and siège=="centré"):
        print("protocole ZAGREB A2")
        print("vos prochains rendez-vous seront  :")
        print("2 dose",j0)
        print("1 dose de sérum en",j0+ datetime.timedelta(days=7),"si l'animal est mort ou en fuite après déclaration")
        print("1 dose",j0+ datetime.timedelta(days=14))
        print("1 dose",j0+ datetime.timedelta(days=28))
        
        #insertion db 
        r1=j0.strftime('%Y-%m-%d')
        r2=(j0+ datetime.timedelta(days=3)).strftime('%Y-%m-%d')
        r3=(j0+ datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        r4=(j0+ datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        r5=(j0+ datetime.timedelta(days=28)).strftime('%Y-%m-%d')
        
        c={"date_vaccination":r1,"numero_lot":v["numero_lot"],"nombre_dose":2,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r3,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r4,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r5,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        
        
    elif (profondeur=="pronfonde" and (nombre=="multiple" or nombre=="unique")  or siège in list_extrémité):
        print("protocole ESSEN A1")
        print("une dose de sérum le:",j0)
        print("vos prochains rendez-vous seront  :")
        print("1 dose",j0)
        print("1 dose",j0+ datetime.timedelta(days=3))
        print("1 dose",j0+ datetime.timedelta(days=7))
        print("1 dose",j0+ datetime.timedelta(days=14))
        print("1 dose",j0+ datetime.timedelta(days=28))
        #insertion db
        r1=j0.strftime('%Y-%m-%d')
        r2=(j0+ datetime.timedelta(days=3)).strftime('%Y-%m-%d')
        r3=(j0+ datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        r4=(j0+ datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        r5=(j0+ datetime.timedelta(days=28)).strftime('%Y-%m-%d')
        
        c={"date_vaccination":r1,"numero_lot":v["numero_lot"],"nombre_dose":2,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r2,"numero_lot":v["numero_lot"],"nombre_dose":2,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r3,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r4,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r5,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        
    elif (profondeur=="pronfonde" or (nombre=="multiple" or nombre=="unique")  or siège in list_extrémité):
        print("protocole ESSEN A1")
        print("une dose de sérum le:",j0)
        print("vos prochains rendez-vous seront  :")
        print("1 dose",j0)
        print("1 dose",j0+ datetime.timedelta(days=3))
        print("1 dose",j0+ datetime.timedelta(days=7))
        print("1 dose",j0+ datetime.timedelta(days=14))
        print("1 dose",j0+ datetime.timedelta(days=28))
        #insertion db
        r1=j0.strftime('%Y-%m-%d')
        r2=(j0+ datetime.timedelta(days=3)).strftime('%Y-%m-%d')
        r3=(j0+ datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        r4=(j0+ datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        r5=(j0+ datetime.timedelta(days=28)).strftime('%Y-%m-%d')
        
        c={"date_vaccination":r1,"numero_lot":v["numero_lot"],"nombre_dose":2,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r2,"numero_lot":v["numero_lot"],"nombre_dose":2,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r3,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r4,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r5,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"]) 
        
    
elif etat=="non observable":
    if(profondeur=="superficielle" and(nombre=="unique") and siège=="centré"):
        print("protocole ZAGREB B2")
        print("vos dates de vaccin seront  :")
        print("2 dose le",j0)
        print("1 dose",j0+ datetime.timedelta(days=7))
        print("1 dose",j0+ datetime.timedelta(days=14))
        print("1 dose",j0+ datetime.timedelta(days=28))
        #insertion db
        r1=j0.strftime('%Y-%m-%d')
        r2=(j0+ datetime.timedelta(days=3)).strftime('%Y-%m-%d')
        r3=(j0+ datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        r4=(j0+ datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        r5=(j0+ datetime.timedelta(days=28)).strftime('%Y-%m-%d')
        
        c={"date_vaccination":r1,"numero_lot":v["numero_lot"],"nombre_dose":2,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r3,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r4,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r5,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        
        
        
    elif (profondeur=="pronfonde" or (nombre=="multiple" or nombre=="unique") or siège in list_extrémité):
        print("protocole ESSEN B1")
        print("vos prochains rendez-vous seront  :")
        print("1 dose",j0)
        print("1 dose",j0+ datetime.timedelta(days=3))
        print("1 dose",j0+ datetime.timedelta(days=7))
        print("1 dose",j0+ datetime.timedelta(days=14))
        print("1 dose",j0+ datetime.timedelta(days=28))
        #insertion dans vaccination
        r1=j0.strftime('%Y-%m-%d')
        r2=(j0+ datetime.timedelta(days=3)).strftime('%Y-%m-%d')
        r3=(j0+ datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        r4=(j0+ datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        r5=(j0+ datetime.timedelta(days=28)).strftime('%Y-%m-%d')
        
        c={"date_vaccination":r1,"numero_lot":v["numero_lot"],"nombre_dose":2,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r2,"numero_lot":v["numero_lot"],"nombre_dose":2,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r3,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r4,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
        c={"date_vaccination":r5,"numero_lot":v["numero_lot"],"nombre_dose":1,"patient_id":cin}
        insertVaccination(c["date_vaccination"],c["numero_lot"],c["nombre_dose"],c["patient_id"])
    
        
        
        
# vérification du la validité du vaccin dlc et quantité

# convert from string format to datetime format

datetime = datetime.datetime.strptime(v["dlc_vaccin"], format)
xv=10 # un minimum de 10 dose de vaccin est la limite à ne pas dépasser du stock de vaccin
qv=int(v["quantite"])
if datetime.date()>j0 and qv>xv:
    print("vaccin validé")
else:
    print("vaccin périmé")  
      


#les conditions de sérothérapie
#test sur le type du sérum antirabique disponible(à transformer sur le tableau)        
if SAR=="equirab":
    if poid<75:
        dose=poid/3
        dose=round(dose,2)
        print("la dose totale du SAR est:",dose,"ml")
    else:
        dose=15
        dose=round(dose,2)
        print("la dose totale du SAR est:",dose,"ml")
elif SAR=="gammarab":
    if poid<90:
        dose=poid/5
        dose=round(dose,2)
        print("la dose totale du SAR est:",dose,"ml")
    else:
        dose=30
        dose=round(dose,2)
        print("la dose totale du SAR est:",dose,"ml")
        

        

#test besredka
# première partie
print("première partie du test besredka: injection de 0.1ml de SAR intradermique") 
            
#input taille papule , rougeur_autour, réaction
          
taille_papule=0 ;
taille_papule=int(input("donner la taille de papule du patient en millimètres(veuillez saisir un entier):"))
print(taille_papule,"mm")

rougeur_autour=0 ;
rougeur_autour=int(input("donner la rougeur_autour de la lésion en cm(veuillez saisir un entier):"))
print(taille_papule,"cm")

choix=["oui","non"] 
reaction=""
test1=False
while reaction not in choix :
    reaction=input("réaction observée (oui/non):")
print(reaction) 
if (taille_papule< 10 and rougeur_autour<2.5 and reaction=="non") :
        test1==True;
        print("passer au deuxième test! 0.25ml de SAR en sous_cutanée") 
                    
#deuxième partie du test besredka 

        choix=["oui","non"]
        reaction_local=""
        reaction_generale=""
        while  (reaction_local not in choix) and (reaction_generale not in choix):
            reaction_local=input("y'a t'il une reaction local après 15 min de l'administration?(oui/non):")
            reaction_generale=input("y'a t'il une reaction générale après 15 min de l'administration?(oui/non):")
        print(reaction_generale)
        print(reaction_local)   
         
        if (((reaction_local=="non")==True) and  ((reaction_generale=="non")==True)) :
            print("test besredka négatif!") ;
            dose=dose-0.35
            dose=round(dose,2)
            print(" la dose de sérum à administrer le",j0,"est",dose,"ml") 
            #test sur la distribution de la dose du SAR
            local=0
            glob=0
            while local+glob!=dose:
                print("veuillez respecter la dose préscrite!")
                local=float(input("quantité locale:"))
                glob=float(input("quantité global:"))
        else:
            print("ATTENTION! patient allergique au SAR!!!!!!!! ") 
else:
    print("ATTENTION! patient allergique au SAR! ")
      
      

# insertion dans la table sérothérapie de db 


s={"dose_id":dose_id,"dose_total":dose,"date_administration":r1,"quantité_local":local,"quantite_generale":glob,"patient_id":cin,"numero_lot":dose_id}

insertSerotherapie(s["dose_id"],s["dose_total"],s["date_administration"],s["quantité_local"],s["quantite_generale"],s["patient_id"],s["numero_lot"])

#affichage des deux tableaux sérothérapie et vaccination 
print("vaccination:")
vac={}
x= getVaccination(1)
for i in x: 
    print(i)
vac=i

print("serothérapie")

ser={}
x= getSerotherapie(1)
for i in x: 
    print(i)
ser=i