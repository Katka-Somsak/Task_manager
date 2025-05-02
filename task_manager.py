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
            task = {"nazev": nazev_1, "popis": popis_1}
            ukoly.append(task)
            return f"Úkol '{nazev_1}' byl přidán.\n"
        else:
            print("Pole název a popis nesmí být prázdné!")

def zobrazit_ukoly():
    zobrazit = ""
    if not ukoly:
        return f"\nSeznam úkolů:\nŽádné uložené úkoly\n"
    for index, row in enumerate(ukoly, start=1):
        zobrazit += f"{index}. {row["nazev"]} - {row["popis"]}\n"
    return f"\nSeznam úkolů:\n{zobrazit}\n"

def odstranit_ukol():
    while True:
        vstup_3 = input(f"\n{zobrazit_ukoly()}\n\nZadejte číslo úkolu, který chcete odstranit: ")
        if vstup_3.isnumeric() and int(vstup_3) in range(1, len(ukoly)+1):
            vstup_3 = int(vstup_3)
            zmazany_ukol = ukoly[vstup_3-1]["nazev"]
            ukoly.pop(vstup_3-1)
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
            break
    
if __name__ == "__main__":    
    hlavni_menu()