"""
main.py: Čtvrtý projekt do Engeto Online Python Akademie

author: Kamil Mach
email: kamil.machuj@gmail.com

"""

# gl. seznam pro ukoly
ukoly = []

def hlavni_menu():
    while True:
        print("\n--- Hlavní menu ---")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyberte možnost 1-4: ")
        
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Program ukončen.\n")
            break
        else:
            print(f"\n", {volba},"Je neplatná volba, zkuste to znovu.\n")

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("\nNázev úkolu nesmí být prázdný. Zkuste to znovu.\n")
            continue
        
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("\nPopis úkolu nesmí být prázdný. Zkuste to znovu.\n")
            continue
        
        ukoly.append({"nazev": nazev, "popis": popis})
        # print(f"Úkol '{nazev}' byl přidán.")2
        break
        

def zobrazit_ukoly():
    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
    else:
        print("\n--- Seznam úkolů ---")
        for idx, ukol in enumerate(ukoly, start=1):
            print(f"{idx}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol():
    if not ukoly:
        print("\nSeznam úkolů je prázdný. Není co odstranit.\n")
        return
    
    zobrazit_ukoly()
    while True:
        try:
            cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo <= len(ukoly):
                odebrany_ukol = ukoly.pop(cislo - 1)
                print(f"Úkol '{odebrany_ukol['nazev']}' byl odstraněn.")
                break
            else:
                print(f"\n", {cislo}, "\nNeplatné nebo neexistující číslo úkolu. Zkuste to znovu.\n")
        except ValueError:
            print(f"\n", {cislo}, "Neplatný vstup. Zadejte číslo.\n")

if __name__ == "__main__":
    hlavni_menu()