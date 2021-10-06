import random

list = ["oranje", "blauw", "groen", "bruin"]
Zak = []
def fill_bag():
    aantal = int(input("Hoeveel moeten er in de zak?"))
    while aantal > 0:
        kleur = random.choice(list)
        Zak.append(kleur)
        aantal -= 1
    print("De zak M&M bevat:")
    print(Zak)
fill_bag()