import eel
from datetime import datetime

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
        uj_termek["cikkszam"] = mezok[0]
        uj_termek["kategoria"] = mezok[1]  # kategória
        uj_termek["gyarto"] = mezok[2]  # gyártó
        uj_termek["termeknev"] = mezok[3]  # terméknév
        uj_termek["ar"] = int(mezok[4])  # ár
        uj_termek["garancia"] = int(mezok[5])  # garancia

        tarolo[mezok[0]] = uj_termek  # cikkszám
    return tarolo

@eel.expose
def create_receipt(products):
    print(products)
    now_date = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    with open(f'{now_date}.TEN', 'w', encoding="utf-8") as f:
        f.write("Gyártó;Darab;Eár\n")
        for product in products:
            f.write(f"{product['articleNumber']};{product['piece']};{product['price']}\n")

# Start the index.html file
eel.start("index.html")