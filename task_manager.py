import sys

spravce_ukolu = {
    1: "Přidat nový úkol",
    2: "Zobrazit všechny úkoly",
    3: "Odstranit úkol",
    4: "Konec Programu"
} 

ukoly = []

def pridat_ukol():
    while True:
        nazev_1 = input("\nZadejte název úkolu: ")
        popis_1 = input("Zadejte popis úkolu: ")
        if nazev_1.strip() and popis_1.strip():
            nazev_1 = nazev_1.replace(" - ", "-")
            ukoly.append(f"{nazev_1} - {popis_1}")
            vysledek_1 = f"Úkol '{nazev_1}' byl přidán.\n"
            return vysledek_1
        else:
            print("Pole název a popis nesmí být prázdné!")
        

def zobrazit_ukoly():
    zobrazit = ""
    for index, row in enumerate(ukoly, start=1):
        zobrazit += f"{index}. {row}\n"
    vysledek_2 = f"\nSeznam úkolů:\n{zobrazit}\n"
    return vysledek_2


def odstranit_ukol():
    zobrazit = ""
    for index, row in enumerate(ukoly, start=1):
        zobrazit += f"{index}. {row}\n"
    while True:
        vysledek_3 = input(f"\nSeznam úkolů:\n{zobrazit}\n\nZadejte číslo úkolu, který chcete odstranit: ")
        if vysledek_3.isnumeric() and int(vysledek_3) in range(1, len(ukoly)+1):
            vysledek_3 = int(vysledek_3)
            zmazany_ukol = (ukoly[vysledek_3-1]).split(" - ")
            zmazany_ukol = zmazany_ukol[0]
            ukoly.pop(vysledek_3-1)
            return f"Úkol '{zmazany_ukol}' byl odstraněn.\n"
        else:
            print("\nNeznáme číslo úkolu. Zadejte znovu.")


def hlavni_menu(): 
    while True:
        hlavicka_menu = ""
        for key, value in spravce_ukolu.items():
            hlavicka_menu += f"{key}. {value}\n" 
        dotaz = input(f"Správce úkolů - Hlavní menu\n{hlavicka_menu}Vyberte možnost (1-{len(spravce_ukolu)}): ")
        while not (dotaz.isnumeric() and int(dotaz) in range(1, len(spravce_ukolu)+1)):
            print("ZADEJTE PLATNÝ VSTUP")
            dotaz = input(f"Vyberte možnost (1-{len(spravce_ukolu)}): ")

        dotaz = int(dotaz)
        if dotaz == 1:
            print(pridat_ukol())
            continue
        elif dotaz == 2:
            print(zobrazit_ukoly())
            continue
        elif dotaz == 3:
            print(odstranit_ukol())
            continue
        else:
            print("\nKonec programu")
            sys.exit()
    
    
hlavni_menu()