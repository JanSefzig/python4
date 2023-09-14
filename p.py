


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
