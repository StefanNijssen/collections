import random

list = ["oranje", "blauw", "groen", "bruin"]
Zak = []
def fill_bag_List():
    aantal = int(input("Hoeveel moeten er in de zak?"))
    while aantal > 0:
        kleur = random.choice(list)
        Zak.append(kleur)
        aantal -= 1
    return("De zak M&M bevat:" + Zak)


mnmDictionaryBag = {
  
}

def fill_bag_Dic():
  aantal = int(input("Hoveel M&M's moeten er in de zak?"))
  list = ["rood", "geel", "bruin"]
  while aantal > 0:
      kleur = random.choice(list)
      mnmDictionaryBag[kleur] = mnmDictionaryBag.get(kleur, 0) + 1

      aantal -= 1
  return(mnmDictionaryBag)



def fill_bag():
    fill_bag_Dic()
    fill_bag_List()

