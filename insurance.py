class Pojisteni:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} {self.vek} {self.telefon}"


def vytvor_pojisteni():

    jmeno = input("Zadej jméno: ").strip()
    while not jmeno.isalpha() or not jmeno:
        print("Jméno nesmí obsahovat čísla ani být prázdné.\n")
        jmeno = input("Zadej jméno: ").strip()

    prijmeni = input("Zadej příjmení: ").strip()
    while not prijmeni.isalpha() or not prijmeni:
        print("Příjmení nesmí obsahovat čísla nebo být prázdné.\n")
        prijmeni = input("Zadej příjmení: ").strip()


    while True:
        try:
            vek = int(input("Zadejte věk: ").strip())
            if vek <=0:
                raise ValueError
            break
        except ValueError:
            print("Věk musí být kladné číslo")

    flag = False
    while not flag:
        telefon = (input("Zadejte telefonní číslo: +420 "))
        if len(telefon) == 9 and telefon.isdigit():
            flag = True
        else:
            print("Špatné telefonní číslo. Zadejte číslo ve formátu +420 XXXXXXXXX\n")

    return Pojisteni(jmeno, prijmeni, vek, telefon)


def vypis_pojisteneho(pojisteni):
    print(pojisteni)


def vypis_pojistenych(pojisteni):
    for pojisteny in pojisteni:
        print(str(pojisteny))


def vyhledej_pojisteneho(pojisteni):
    jmeno = input("Zadej jméno: ").strip()
    prijmeni = input("Zadej příjmení: ").strip()
    found = False
    for pojisteny in pojisteni:
        if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
            vypis_pojisteneho(pojisteny)
            found = True
    if not found:
        print (f"Nenalezen žádný pojištěný s jménem '{jmeno}' a příjměním '{prijmeni} ' ")


def main():
    pojisteni = []
    while True:
        print("1. Vytvořit pojištění\n")
        print("2. Zobrazení seznamu všech pojištěných\n")
        print("3. Vyhledání pojištěného podle jména a příjmení\n")
        print("4. Konec")
        volba = input("Zadej volbu: ")
        if volba == "1":
            pojisteni.append(vytvor_pojisteni())
        elif volba == "2":
            vypis_pojistenych(pojisteni)
        elif volba == "3":
            vyhledej_pojisteneho(pojisteni)
        elif volba == "4":
            break
        else:
            print("Neplatná volba")


main()