'''import os

def betolt_szotarak_szotaraba(tarolo):

    fajl = open(file="Terméklista.csv", mode="tr")
    sorok = fajl.readlines()
    fajl.close()

    del sorok[0]

    for sor in sorok:
        mezok = sor.split(";")

        uj_termek = {}
        uj_termek["kategoria"] = mezok[1]  # kategória
        uj_termek["gyarto"] = mezok[2]  # gyártó
        uj_termek["termeknev"] = mezok[3]  # terméknév
        uj_termek["ar"] = int(mezok[4])  # ár
        uj_termek["garancia"] = int(mezok[5])  # garancia

        tarolo[mezok[0]] = uj_termek  # cikkszám

def osszegez(tetelek):
    szum=0
    # ???
    return szum

def letezo_termek(tarolo, cikkszam):
    van_ilyen=False
    # ???
    #  Mikor teljesül, az hogy:   van_ilyen=True
    return van_ilyen

szotarak_szotara = {}
betolt_szotarak_szotaraba(szotarak_szotara)

nyugta_tetelei = []

os.system('cls')
keresett_cikkszam = "_"
while keresett_cikkszam != "":

    print(f"Eddigi tételek száma: {len(nyugta_tetelei)} db, értékük : {osszegez(nyugta_tetelei)} Ft")

    keresett_cikkszam = input("\nKérem a termék cikkszámát! :")
    if keresett_cikkszam == "":  # befejezés
        break

    if letezo_termek(szotarak_szotara, keresett_cikkszam):
#    if letezo_termek(listaban_szotarak, keresett_cikkszam):
#    if letezo_termek(szotarak_szotara, keresett_cikkszam):
        mennyiseg = int(input("\nKérem az eladási mennyiséget! :"))
        eladasi_ar = int(input("Kérem az eladási árat! :"))
        nyugta_tetelei.append([keresett_cikkszam, mennyiseg, eladasi_ar])
    else:
        print("\nHIBA: Nem létező cikkszám!")

print(nyugta_tetelei)'''

import eel
from random import randint

eel.init("web")


# Exposing the random_python function to javascript
@eel.expose
def read_from_file():
    tarolo = {}
    fajl = open(file="Terméklista.csv", mode="tr")
    sorok = fajl.readlines()
    fajl.close()

    del sorok[0]

    for sor in sorok:
        mezok = sor.split(";")

        uj_termek = {}
        uj_termek["kategoria"] = mezok[1]  # kategória
        uj_termek["gyarto"] = mezok[2]  # gyártó
        uj_termek["termeknev"] = mezok[3]  # terméknév
        uj_termek["ar"] = int(mezok[4])  # ár
        uj_termek["garancia"] = int(mezok[5])  # garancia

        tarolo[mezok[0]] = uj_termek  # cikkszám
    return tarolo
# Start the index.html file
eel.start("index.html")