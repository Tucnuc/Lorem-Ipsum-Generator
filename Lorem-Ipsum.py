import random
import time
import textwrap
import os

nevim = []

delka_odstavce = 0
max_delka = 0
odstavce = 0
delka_radku = 0
vsechny_odstavce = []

ostrava = ("rožnout","chachar","pyčo","grcat","bo","bulat","hrča","najebat","kobzole","kaj","včil","chuj","cyp","bazaly","roba","šufan","kajsyk","pazury","štrample","štrample","kura","robit","dupa","mňamka","šupina","pivoň","fofr")
brno = ("pindy","čapy","budka","bagrovat","šalina","špilas","bazmek","krýgl","merka","brajgl","dovalit","békať","svišť","vyfičet","šméčko","čubrnět","špica","róry","hrnót","krtek","slintáč","hokna","rychna","betla","šlohnót")
hana = ("cecan","ošmóranec","ohonit","šošeň","otěkat","šak","šiblé","šklibit","šléšky","šmédit","šmodrcha","špičák","šršňák","orál","čapa","řbet","čuňa","bék","brňák","brikule","céch","loskanec","máčka","masenko","mrčet","nigde")
ostatni = ('dolor','sit','amet','consectetur','adipiscing','elit','sed','do','eiusmod','tempor','incididunt','ut','labore','et','dolore','magna','aliqua','ut','enim','ad','minim','veniam','quis','nostrud','exercitation','ullamco','laboris','nisi')
nareci = ostrava

zapnuti = input("Zmáčkněte Enter pro zapnutí: ")
if zapnuti.strip() == "":
    print("Vítejte. \033[3m*windows zapnutí sound effect*\033[0m")
    print("")
    time.sleep(2)
    nevim.append("check")
elif zapnuti:
    print("Na shledanou. \033[3m*windows vypnutí sound effect*\033[0m")

while True:
    if "check" in nevim:
        print("Zdraví tě, \033[1mLorem Ipsum Generátor 3000 DeLuxe++\033[0m.")
        time.sleep(1.5)
        print("Děkujeme, že jste si zakoupil Premium verzi, za pouhých \033[1m9.99$\033[0m.")
        time.sleep(1.5)
        print("Úspěšně jste odemknul funkci: \033[1mZvolení nářečí\033[0m")
        time.sleep(1)
        print("Gratulujeme!")
        print("")
        time.sleep(2)
        nevim.remove("check")
        nevim.append("setup")

    if "setup" in nevim:
        delka_slov = int(input("Zadejte prosím maximální délku slov: "))
        max_delka += delka_slov
        print("Zpracovávám...")
        print("")
        time.sleep(1)
        pocet_znaku = int(input("Zadejte prosím, kolik odhadem chcete slov na jednom řádku: "))
        delka_radku += (pocet_znaku*6)
        print("Zpracovávám...")
        print("")
        time.sleep(1)
        pocet_slov = int(input("Teď zadejte, kolik slov se bude nacházet v jednom odstavci: "))
        delka_odstavce += pocet_slov
        print("Zpracovávám...")
        print("")
        time.sleep(1)
        pocet_odstavcu = int(input("Nyní zadejte kolik odstavců chcete vygenerovat: "))
        odstavce += pocet_odstavcu
        print("Zpracovávám...")
        print("")
        time.sleep(1)
        volene_nareci = str(input("\033[1mPREMIUM FUNKCE:\033[0m Zvolte prosím typ nářečí [1 - Ostravské, 2 - Brněnské, 3 - Hanácké]: "))
        if volene_nareci == 1:
            nareci = ostrava
        elif volene_nareci == 2:
            nareci = brno
        elif volene_nareci == 3:
            nareci = hana
        print("Zpracovávám...")
        print("")
        time.sleep(1)
        nevim.remove("setup")
        nevim.append("magic")

    if "magic" in nevim:
        for _ in range(odstavce):
            vybrane_slova = [slovo for slovo in nareci if len(slovo) <= max_delka]
            vybrana_matlanina = [slovo for slovo in ostatni if len(slovo) <= max_delka]
            final_slova = []
            for _ in range(delka_odstavce):
                cislo = random.randint(0,20)
                cislo2 = random.randint(0,12)
                cislo3 = random.randint(0,2)
                losovane_slova = random.choice(vybrane_slova)
                if cislo3 == 1:
                    losovane_slova = random.choice(vybrana_matlanina)
                if cislo == 3 and cislo2 != 4:
                    losovane_slova += ","
                if cislo2 == 4 and cislo != 3:
                    losovane_slova += "."
                final_slova.append(losovane_slova)
            final_text = textwrap.fill(' '.join(final_slova), width=delka_radku)
            final_text = final_text.capitalize()
            final_text += "."
            vsechny_odstavce.append(final_text)
            alfa_text = "\n\n".join(vsechny_odstavce)

        gamma_text = ""
        tecka = 0
        for T in alfa_text:
            if tecka < 1:
                gamma_text += T
            else:
                gamma_text += T.upper()
            if T == ".":
                tecka = 2
            else:
                tecka += -1

        beta_text = gamma_text
        beta_text += "\n\n\033[3mVytvořeno \033[1mLorem Ipsum Generátorem 3000 DeLuxe++\033[0m\033[0m"
        print("Generuji...")
        print("")
        time.sleep(1)
        print(beta_text)
        
        time.sleep(2)
        print("")
        open1 = int(input("Chcete vytvořit a otevřít textový dokument s vygenerovaným textem? [1 - ano, 2 - ne]: "))
        if open1 == 1:
            with open('vystup.txt', 'w') as f:
                f.write(gamma_text)
            time.sleep(0.2)
            os.system("notepad.exe vystup.txt")
            break
        else:
            break
