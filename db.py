import pymongo  #pip3 install pymongo

# Create instance database
def createDb():
    client = pymongo.MongoClient("localhost", 27017)
    db = client.traitement
    print(db)
    return db


# Insert functions
def insertPatient(cin, nom, prenom, numero):
    patient = {
    "cin" : cin,
    "nom" : nom,
    "prenom" : prenom,
    "numero" : numero
    }
    db["patient"].insert_one(patient)

def insertVaccin(dlc_vaccin, numero_lot, quantite):
    vaccin = {
        "dlc_vaccin": dlc_vaccin, # date
        "numero_lot": numero_lot,
        "quantite": quantite
    }
    db["vaccin"].insert_one(vaccin)


def insertSerum(dlc_serum, numero_lot, quantite, type_serum):
    serum = {
        "dlc_serum": dlc_serum, # date
        "numero_lot": numero_lot,
        "quantite": quantite,
        "type_serum": type_serum
    }
    db["serum"].insert_one(serum)


def insertVaccination(date_vaccination, numero_lot, nombre_dose, patient_id):
    vaccination = {
        "date_vaccination": date_vaccination, # date type
        "numero_lot": numero_lot,
        "nombre_dose": nombre_dose,
        "patient_id": patient_id,
    }
    db["vaccination"].insert_one(vaccination)

def insertSerotherapie(dose_id, dose_total, date_administration, quantite_local, quantite_generale, patient_id, numero_lot):
    serotherapie = {
        "dose_id": dose_id,
        "dose_total": dose_total,
        "date_administration": date_administration, # date type
        "quantite_local": quantite_local,
        "quantite_generale": quantite_generale,
        "patient_id": patient_id,
        "numero_lot": numero_lot
    }
    db["serotherapie"].insert_one(serotherapie)

# Update functions
def updatePatient(oldPatient, cin, nom, prenom, numero):
    newPatient = { "$set": { 
        "cin" : cin,
        "nom" : nom,
        "prenom" : prenom,
        "numero" : numero } }
    db["patient"].update_one(oldPatient, newPatient)

def updateVaccin(oldVaccin, dlc_vaccin, numero_lot, quantite):
    newVaccin = { "$set": {
        "dlc_vaccin": dlc_vaccin,
        "numero_lot": numero_lot,
        "quantite": quantite
    }}
    db["vaccin"].update_one(oldVaccin, newVaccin)


def updateSerum(oldSerum, dlc_serum, numero_lot, quantite, type_serum):
    newSerum = { "$set": {
        "dlc_serum": dlc_serum,
        "numero_lot": numero_lot,
        "quantite": quantite,
        "type_serum": type_serum
    }}
    db["serum"].update_one(oldSerum, newSerum)


def updateVaccination(oldVaccination, date_vaccination, numero_lot, nombre_dose, patient_id):
    newVaccination = { "$set": {
        "date_vaccination": date_vaccination,
        "numero_lot": numero_lot,
        "nombre_dose": nombre_dose,
        "patient_id": patient_id,
    }}
    db["vaccination"].insert_one(oldVaccination, newVaccination)

def updateSerotherapie(oldSerotherapie, dose_id, dose_total, date_administration, quantite_local, quantite_generale, patient_id, numero_lot):
    newSerotherapie = { "$set": {
        "dose_id": dose_id,
        "dose_total": dose_total,
        "date_administration": date_administration,
        "quantite_local": quantite_local,
        "quantite_generale": quantite_generale,
        "patient_id": patient_id,
        "numero_lot": numero_lot
    }}
    db["serotherapie"].update_one(oldSerotherapie, newSerotherapie)

# Delete functions
def deletePatient(patient):
    db["patient"].delete_one(patient)

def deleteVaccin(vaccin):
    db["vaccin"].delete_one(vaccin)


def deleteSerum(serum):
    db["serum"].delete_one(serum)


def deleteVaccination(vaccination):
    db["vaccination"].delete_one(vaccination)

def deleteSerotherapie(serotherapie):
    db["serotherapie"].delete_one(serotherapie)


# Get functions
def getPatients():
    return db["patient"].find()

def getPatientByCin(cin):
    return db["patient"].find({"cin": cin})

def getVaccins():
    return db["vaccin"].find()

def getVaccinByNmLot(numero_lot):
    return db["vaccin"].find({"numero_lot": numero_lot})

def getSerum():
    return db["serum"].find()

def getSerumByNmLot(numero_lot):
    return db["serum"].find({"numero_lot": numero_lot})

def getVaccination(vaccination):
    return db["vaccination"].find()

def getSerotherapie(serotherapie):
    return db["serotherapie"].find()

db = createDb()



"""



x = getPatients()
for i in x:
    print(i)

x = getPatientByCin(1111)
for i in x:
    a = i
    print(i)

deletePatient(a)


x = getPatients()
for i in x:
    print(i)

"""