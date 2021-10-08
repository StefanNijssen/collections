import random
mnmDictionaryBag = {
  
}

def fill_bag():
  aantal = int(input("Hoveel M&M's moeten er in de zak?"))
  list = ["rood", "geel", "bruin"]
  while aantal > 0:
      kleur = random.choice(list)
      mnmDictionaryBag[kleur] = mnmDictionaryBag.get(kleur, 0) + 1

      aantal -= 1
  print(mnmDictionaryBag)
fill_bag()
