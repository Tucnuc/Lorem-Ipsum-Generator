# Lorem-Ipsum-Generator

## V čem je tento lorem ipsum generátor jiný od ostatních?
Můžete si totiž zvolit jaké chcete **nářečí** ve vygenerovaném textu. Je na výběr Ostravské, Brněnské a Hanácké. Dodá to vašemu vygenerovanému textu víc _živější_ pocit. <br/><br/>
Kromě toho se dá generace nastavit například podle:

* Maximální délka slov <br/>
* Jak dlouhý má být jeden řádek pomocí počtu slov <br/>
* Počet slov v odstavci a jejich počet <br/>

Poté je váš text napsán do konzole. Též si můžete nechat vytvořit a otevřít textový dokument s textem připraveným rovnou k použití. <br/><br/>
### Příklad kódu generujícího text: <br/>
```
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
```
