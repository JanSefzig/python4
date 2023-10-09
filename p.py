


#7.9
def vytvor_trojuhelnik(x):
    for i in range(1, x + 1, 2):
        mezery = (x - i) // 2
        print(" " * mezery + "x" * i + " " * mezery)


def je_liche_cislo(cislo):
    return cislo % 2 != 0


while True:
    zadane_cislo = input("Zadejte liché číslo X pro vytvoření trojúhelníku: ")
    
    try:
        cislo_x = int(zadane_cislo)
        if je_liche_cislo(cislo_x):
            vytvor_trojuhelnik(cislo_x)
            break
        else:
            print("Zadali jste sudé číslo. Zadejte liché číslo.")
    except ValueError:
        print("Neplatný vstup. Zadejte prosím celé liché číslo.")


def vytvor_radky_cisel(x):
    for i in range(1, 2 * x):
        cislice = " ".join(map(str, range(1, i + 1)))
        print(cislice)


while True:
    zadane_cislo = input("Zadejte liché číslo X: ")
    
    try:
        cislo_x = int(zadane_cislo)
        if cislo_x % 2 != 0:
            vytvor_radky_cisel(cislo_x)
            break
        else:
            print("Zadali jste sudé číslo. Zadejte liché číslo.")
    except ValueError:
        print("Neplatný vstup. Zadejte prosím celé liché číslo.")
#18.9
cisla = [1, 2, 3, 4, 5]
soucet = sum(cisla)
print("Součet všech prvků v seznamu je:", soucet)

cisla = [1, 2, 3, 4, 5]
nejmensi = min(cisla)
nejvetsi = max(cisla)
print("Nejmenší číslo v seznamu je:", nejmensi)
print("Největší číslo v seznamu je:", nejvetsi)

cisla = [1, 2, 2, 3, 4, 4, 5, 5]
cisla = list(set(cisla))
print("Seznam bez duplikátů:", cisla)

cisla = []
if not cisla:
    print("Seznam je prázdný.")
else:
    print("Seznam není prázdný.")






#25.9
keys = ["John", "Marie", "Alex"]
values = ["41", "15", "66"]

slovnik = dict(zip(keys, values))
print(slovnik)

trida = {
    "student1": {"jmeno": "John", "vek": 18},
    "student2": {"jmeno": "Marie", "vek": 19},
    "student3": {"jmeno": "Alex", "vek": 17},
    "student4": {"jmeno": "Eva", "vek": 20},
    "student5": {"jmeno": "Daniel", "vek": 18}
}


#2.10
zamestnanci = {
    "zamestnanec1": {"jmeno": "John", "prijmeni": "Doe", "pozice": "Manažer", "email": "john.doe@example.com", "kancelar": "A101"},
    "zamestnanec2": {"jmeno": "Jane", "prijmeni": "Smith", "pozice": "Vývojář", "email": "jane.smith@example.com", "kancelar": "B203"},
    "zamestnanec3": {"jmeno": "Alice", "prijmeni": "Johnson", "pozice": "Asistentka", "email": "alice.johnson@example.com", "kancelar": "A101"},
    "zamestnanec4": {"jmeno": "Bob", "prijmeni": "Brown", "pozice": "Vývojář", "email": "bob.brown@example.com", "kancelar": "C305"},
    "zamestnanec5": {"jmeno": "Eva", "prijmeni": "Williams", "pozice": "Vedoucí projektu", "email": "eva.williams@example.com", "kancelar": "B203"}
}

for zamestnanec, informace in zamestnanci.items():
    print(f"Zaměstnanec: {zamestnanec}")
    print(f"Jméno: {informace['jmeno']} {informace['prijmeni']}")
    print(f"Pozice: {informace['pozice']}")
    print(f"Email: {informace['email']}")
    print(f"Kancelář: {informace['kancelar']}")
    print()

for zamestnanec, informace in zamestnanci.items():
    print(f"{informace['jmeno']} {informace['prijmeni']}, Email: {informace['email']}")

zamestnanec = "zamestnanec3"  # Zde zvolte konkrétního zaměstnance
informace = zamestnanci.get(zamestnanec)

if informace:
    print(f"Jméno: {informace['jmeno']} {informace['prijmeni']}")
    print(f"Pozice: {informace['pozice']}")
else:
    print("Zaměstnanec nebyl nalezen.")

kancelar = "A101"  # Zde zvolte konkrétní kancelář
for zamestnanec, informace in zamestnanci.items():
    if informace['kancelar'] == kancelar:
        print(f"{informace['jmeno']} {informace['prijmeni']}, Pozice: {informace['pozice']}")





















#11.9
def vytvor_obrazec_x(velikost):
    for i in range(velikost):
        for j in range(velikost):
            if i == j or i + j == velikost - 1:
                print("1", end="")
            else:
                print("ㅤ", end="")
        print()


def je_liche_cislo(cislo):
    return cislo % 2 != 0


while True:
    zadane_cislo = input("Zadejte liché číslo Z: ")
    
    try:
        cislo_z = int(zadane_cislo)
        if je_liche_cislo(cislo_z):
            vytvor_obrazec_x(cislo_z)
            break
        else:
            print("Zadali jste sudé číslo. Zadejte liché číslo.")
    except ValueError:
        print("Neplatný vstup. Zadejte prosím celé liché číslo.")

#9.10
def vypis_jmena():
    with open('names.txt', 'r') as file:
        for line in file:
            print(line.strip())

def pridat_jmena(jmena):
    with open('names.txt', 'a') as file:
        for jmeno in jmena:
            file.write(jmeno + '\n')

# Zavolání funkcí:
vypis_jmena()
nova_jmena = ['Marta', 'Petr', 'Eva']
pridat_jmena(nova_jmena)

def pocet_slov_v_souboru(nazev_souboru):
    with open(nazev_souboru, 'r') as file:
        text = file.read()
        slova = text.split()
        return len(slova)

# Zavolání funkce a vypsání počtu slov
pocet = pocet_slov_v_souboru('names.txt')
print(f'Počet slov v souboru: {pocet}')

import json

# Vytvoření slovníku z obrazku (nahraďte obsahem obrazku)
obrazek_slovniku = {
    "klic1": "hodnota1",
    "klic2": "hodnota2",
    "klic3": "hodnota3"
}

# Zápis slovníku do souboru v JSON formátu
with open('slovnik.txt', 'w') as file:
    json.dump(obrazek_slovniku, file)
