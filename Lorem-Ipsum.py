import random
import time
import textwrap

nevim = ["magic"]

delka_odstavce = 50
max_delka = 10
odstavce = 3
delka_radku = 90
vsechny_odstavce = []

ostrava = ("rožnout","chachar","pyčo","grcat","bo","bulat","hrča","najebat","kobzole","kaj","včil","chuj","cyp","bazaly","roba","šufan","kajsyk","pazury","štrample","štrample","kura","robit","dupa","mňamka","šupina","pivoň","fofr")
brno = ("pindy","čapy","budka","bagrovat","šalina","špilas","bazmek","krýgl","merka","brajgl","dovalit","békať","svišť","vyfičet","šméčko","čubrnět","špica","róry","hrnót","krtek","slintáč","hokna","rychna","betla","šlohnót")
hana = ("cecan","nigdê","ôšmóranec","ôhonit","šôšeň","ôtěkat","šak","šiblé","šklibit","šléšky","šmédit","šmodrcha","špičák","šršňák","ôrál","čapa","řbet","čuňa","bék","brňák","brikule","céch","lêskanec","máčka","masenko","mrčet","nigde")


# zapnuti = input("Zmáčkněte Enter pro zapnutí: ")
# if zapnuti.strip() == "":
#     print("Vítejte. \033[3m*windows zapnutí sound effect*\033[0m")
#     print("")
#     time.sleep(2)
#     nevim.append("check")
# elif zapnuti:
#     print("Na shledanou. \033[3m*windows vypnutí sound effect*\033[0m")

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
        pocet_slov = int(input("Teď zadejte kolik slov se bude nacházet v jednom odstavci: "))
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
        print("Zpracovávám...")
        print("")
        time.sleep(1)
        nevim.remove("setup")
        nevim.append("magic")

    if "magic" in nevim:
        for _ in range(odstavce):
            vybrane_slova = [slovo for slovo in ostrava if len(slovo) <= max_delka]
            final_slova = []
            for _ in range(delka_odstavce):
                losovane_slova = random.choice(vybrane_slova)
                final_slova.append(losovane_slova)
            final_text = textwrap.fill(' '.join(final_slova), width=delka_radku)
            final_text = final_text.capitalize()
            final_text += "."
            vsechny_odstavce.append(final_text)
            alfa_text = "\n\n".join(vsechny_odstavce)

        
        beta_text = alfa_text
        beta_text += "\n\n\033[3mVytvořeno \033[1mLorem Ipsum Generátorem 3000 DeLuxe++\033[0m\033[0m"
        print(beta_text)
        with open('vystup.txt', 'w') as f:
            f.write(alfa_text)
        break


# novy_text += "\n"*2