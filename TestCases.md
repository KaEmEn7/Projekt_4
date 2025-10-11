# Test cases - spuštění programu - prerekvizita pro všechny další testy:


| ID | Název testu | Krok/y | Očekávané chování / výstup | Poznámka | 
| - | - | - | - | - |
| **TC00** | Spuštění programu | Z rootu projektu příkazem `python3 main.py` | Spuštěný program/skript - viditelné menu s nabídkou voleb 1-4 | Prerekvizita pro všechny ostatní testy co předpokládají spuštěný skript/program |

# Test cases - def hlavni_menu():

| ID | Název testu | Vstup (`volba`) | Očekávané chování / výstup |
| - | - | - | - |
| **TC01** | Volba `1` – Přidat nový úkol | "1" | Zavolá funkci `pridat_ukol()`. Po dokončení se zobrazí hlavní menu znovu. |
| **TC02** | Volba `2` – Zobrazit všechny úkoly | `"2"` | Zavolá funkci `zobrazit_ukoly()`. Po zobrazení se vrátí do hlavního menu. |
| **TC03** | Volba `3` – Odstranit úkol | `"3"` | Zavolá funkci `odstranit_ukol()`. Po odstranění úkolu se znovu zobrazí hlavní menu. |
| **TC04** | Volba `4` – Ukončení programu | `"4"` | Vypíše text `Program ukončen.` a ukončí cyklus (`break`). Program končí. |

## Testy chybových hlášek def hlavni_menu():

| ID | Situace | Příčina | Očekávaná reakce systému |
| - | - | - | - |
| **E01** | Uživatel zadá znak mimo rozsah 1–4 | Neodpovídá žádné větvi `if` | Program vypíše chybové hlášení a zůstane v menu |
| **E02** | Uživatel zadá textový nebo prázdný vstup | Neproběhne žádná podmínka `elif` | Program vypíše chybové hlášení a čeká na nový vstup |
| **E03** | Uživatel zadá vstup s mezerami | Vstup se neporovnává se `strip()` hodnotou | Program považuje vstup za neplatný a vypíše chybové hlášení |
| **E04** | Opakované neplatné vstupy | Uživatel opakovaně zadává špatné volby | Program pokaždé vypíše chybu, dokud nebude zadána platná volba |
| **E05** | Uživatel ukončí program správnou volbou  | Zadání `"4"` | Program vypíše „Program ukončen.“ a ukončí běh cyklu |

# Test cases - def pridat_ukol():

| ID | Název testu | Vstup / podmínka | Očekávaný výstup / stav | Poznámka |
| - | - | - | - | - |
| **TC01** | Přidání platného úkolu | Název: „Nakoupit“<br>Popis: „Koupit mléko a chleba“ | Úkol je přidán do seznamu `ukoly` | Seznam má 1 položku s odpovídajícími daty |
| **TC02** | Prázdný název úkolu | Název: `""` (prázdný), poté „Uklidit“<br>Popis: „Vyluxovat obývák“ | Skript vypíše chybu „Název úkolu nesmí být prázdný“ a po opakování úkol přidá | Ověřit, že po první chybě lze zadat znovu |
| **TC03** | Prázdný popis úkolu | Název: „Cvičit“<br>Popis: `""` (prázdný), poté „15 minut běhu“ | Skript vypíše chybu „Popis úkolu nesmí být prázdný“ a po opakování úkol přidá | |
| **TC04** | Trimování mezer | Název: „  Test  “<br>Popis: „  Popis testu  “ | Úkol se přidá bez mezer okolo — názvy by měly být „Test“ a „Popis testu“ | Ověření `.strip()` |
| **TC05** | Zadána hodnota mimo rozsah | `"0"`, `"5"`, `"99"` | Vypíše `Neplatná volba, zkuste to znovu.` a zůstane v hlavním menu. |
| **TC06** | Zadán textový vstup | `"abc"`, `"x"`, `"test"` | Vypíše `Neplatná volba, zkuste to znovu.` a zůstane v hlavním menu. |
| **TC07** | Zadán prázdný vstup | `""` (uživatel stiskne Enter) | Vypíše `Neplatná volba, zkuste to znovu.` a zůstane v hlavním menu. |
| **TC08** | Zadán vstup s mezerami | `"2"` | Vstup nebude oříznut (`"2" != "2"`), proto program vypíše `Neplatná volba, zkuste to znovu.` |
| **TC09** | Zadán vícenásobný vstup | `"1 2"`, `"3 4"` | Program nerozpozná platnou volbu → vypíše `Neplatná volba, zkuste to znovu.` a zůstane v menu. |


# Test cases - def zobrazit_ukoly():

| ID | Název testu | Předpoklad | Očekávané chování / výstup |
| - | - | - | - |
| **TC01** | Zobrazení prázdného seznamu úkolů | `ukoly = []` | Program vypíše `Seznam úkolů je prázdný.` |
| **TC02** | Zobrazení jednoho úkolu | `ukoly = [{"nazev": "Nakoupit", "popis": "Koupit mléko"}]` | Program vypíše:<br>`--- Seznam úkolů ---`<br>`1. Nakoupit - Koupit mléko` |
| **TC03** | Zobrazení více úkolů | `ukoly = [{"nazev": "Uklidit", "popis": "Vyluxovat obývák"}, {"nazev": "Cvičit", "popis": "15 minut běhu"}]` | Program vypíše:<br>`--- Seznam úkolů ---`<br>`1. Uklidit - Vyluxovat obývák`<br>`2. Cvičit - 15 minut běhu` |
| **TC04** | Zobrazení úkolů s prázdným textem v názvu nebo popisu | `ukoly = [{"nazev": "", "popis": "Bez názvu"}, {"nazev": "Bez popisu", "popis": ""}]` | Program vypíše úkoly s prázdnými poli, např.:<br>`1.  - Bez názvu`<br>`2. Bez popisu - ` |
| **TC05** | Správné číslování úkolů | `ukoly` obsahuje 3 položky | Každý úkol je očíslován od 1 výše (`1.`, `2.`, `3.`) |
| **TC06** | Zobrazení úkolů s diakritikou a speciálními znaky     | `ukoly = [{"nazev": "Úklid", "popis": "Umytí nádobí & podlahy"}]` | Text se vypíše správně včetně diakritiky a speciálních znaků |
| **TC07** | Kontrola formátu výpisu | `ukoly = [{"nazev": "Test", "popis": "Popis"}]` | Každý úkol má formát `<pořadí>. <název> - <popis>` |
| **TC08** | Zobrazení po předchozím odstranění úkolů | `ukoly` obsahoval položky, které byly odstraněny, nyní prázdný seznam | Program vypíše `Seznam úkolů je prázdný.` |


# Test cases - def odstranit_ukol():

| ID | Název testu | Předpoklad | Vstup (`cislo`) | Očekávané chování / výstup |
| - | - | - | - | - |
| **TC01** | Odstranění existujícího úkolu | `ukoly = [{"nazev": "Test", "popis": "Popis testu"}]` | `1` | Úkol je odstraněn ze seznamu a vypíše se: `Úkol 'Test' byl odstraněn.` |
| **TC02** | Odstranění úkolu ze seznamu s více položkami | `ukoly = [{"nazev": "A", "popis": "x"}, {"nazev": "B", "popis": "y"}]` | `2` | Druhý úkol je odstraněn, vypíše se `Úkol 'B' byl odstraněn.`, v seznamu zůstane pouze první položka |
| **TC03** | Pokus o odstranění úkolu z prázdného seznamu | `ukoly = []` | *(žádný vstup)* | Vypíše `Seznam úkolů je prázdný. Není co odstranit.` a funkce se ukončí (`return`) |
| **TC04** | Zadání čísla mimo rozsah (větší než počet úkolů) | `ukoly = [{"nazev": "A", "popis": "x"}]` | `5` | Vypíše `Neplatné nebo neexistující číslo úkolu. Zkuste to znovu.` a čeká na další vstup |
| **TC05** | Zadání čísla mimo rozsah (menší než 1) | `ukoly = [{"nazev": "A", "popis": "x"}]` | `0` | Vypíše `Neplatné nebo neexistující číslo úkolu. Zkuste to znovu.` a čeká na nový vstup |
| **TC06** | Zadání nečíselného vstupu | `ukoly = [{"nazev": "A", "popis": "x"}]` | `"abc"` | Vyvolá výjimku `ValueError`, zachytí ji a vypíše `Neplatný vstup. Zadejte číslo.` |
| **TC07** | Zadání prázdného vstupu | `ukoly = [{"nazev": "A", "popis": "x"}]` | `""` | Vyvolá `ValueError`, vypíše `Neplatný vstup. Zadejte číslo.` |
| **TC08** | Zadání platného vstupu po chybě | `ukoly = [{"nazev": "A", "popis": "x"}, {"nazev": "B", "popis": "y"}]` | `"abc"`, poté `1` | Po první chybě vypíše `Neplatný vstup. Zadejte číslo.`, následně po zadání `1` odstraní úkol `A`    |
| **TC09** | Zadání desetinného čísla | `ukoly = [{"nazev": "A", "popis": "x"}]` | `"1.5"`           | Vyvolá `ValueError`, vypíše `Neplatný vstup. Zadejte číslo.` |
| **TC10** | Zadání mezery nebo whitespace | `ukoly = [{"nazev": "Test", "popis": "x"}]` | `"  "` | Vyvolá `ValueError`, vypíše `Neplatný vstup. Zadejte číslo.` |