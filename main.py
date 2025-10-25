"""
main.py: Čtvrtý projekt do Engeto Online Python Akademie

author: Kamil Mach
email: kamil.machuj@gmail.com

"""

# Globální seznam pro ukoly
ukoly = []

def hlavni_menu():
    while True: # Zobrazení hl. menu
        print("\n--- Hlavní menu ---")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyberte možnost 1-4: ") # Získání volbdy od uživatele
        
        # Zpracování volby uživatele
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
            print(f"\n", volba, "Je neplatná volba, zkuste to znovu.\n")

def pridat_ukol():
    while True:
                # Získání názvu úkolu od uživatele
        nazev = input("Zadejte název úkolu: \t\t Pro návrat do hlavní nabídky zadejte kdykoliv 0.\n").strip()
        
        # Kontrola, zda byl zadán název úkolu
        if not nazev:
            print("\nNázev úkolu nesmí být prázdný. Zkuste to znovu.\n")
            continue
        if nazev == "0": # Při zadání 0 se vrátí do hlavního menu
            break
        
        popis = input("Zadejte popis úkolu: ").strip() # Získání popisu úkolu od uživatele

        if popis == 0:
            break
        if not popis:
            print("\nPopis úkolu nesmí být prázdný. Zkuste to znovu.\n")
            continue
        
        ukoly.append({"nazev": nazev, "popis": popis}) # Přidání úkolu do seznamu
        break
        

def zobrazit_ukoly(): # Zobrazí všechny úkoly v seznamu úkolů
    if not ukoly: # Když nejsou ůkoly k zobrazení vypíš hlášku
        print("\nSeznam úkolů je prázdný.")
    else:
        print("\n--- Seznam úkolů ---")
        for idx, ukol in enumerate(ukoly, start=1):
            print(f"{idx}. {ukol['nazev']} - {ukol['popis']}")

# Umožňuje uživateli odstranit úkol ze seznamu úkolů podle jeho čísla.
def odstranit_ukol():
    if not ukoly: # Když nejsou ůkoly k odstranění vypíše hlášku
        print("\nSeznam úkolů je prázdný. Není co odstranit.\n")
        return
    
    zobrazit_ukoly() # Zobrazí seznam úkolů před odstraněním pro zobrazeí možností volby
    while True:
        try:
            cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: \t\t Pro návrat do hlavní nabídky zadejte 0.\n"))
            if 1 <= cislo <= len(ukoly):
                odebrany_ukol = ukoly.pop(cislo - 1) # Odstranění úkolu ze seznamu
                print(f"Úkol '{odebrany_ukol['nazev']}' byl odstraněn.")
                break
            elif cislo == 0: # Při zadání 0 se vrátí do hlavního menu
                break
            else:
                print(f"\nZadali jste neexistující číslo úkolu. Zkuste to znovu.\n")
        except ValueError:
            print(f"\n", "Neplatný vstup. Zadejte číslo úkolu který chcete odstranit.\n")

if __name__ == "__main__":
    hlavni_menu() # Spuštění hlavního menu při spuštění skriptu