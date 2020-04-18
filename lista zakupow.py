zakupy = {
  "piekarnia": ["chleb", "bulki", "paczek"],
  "warzywniak": ["marchew", "seler", "rukola"],
  "warzywniak2": ["marchew", "seler", "rukola"],
  "warzywniak3": ["marchew", "seler", "rukola"],
}
liczebniki = {
  1: "Pierwszy",
  2: "Drugi",
  3: "Trzeci",
}
count = 0
wizyta = 1
for sklep in zakupy:
  #print("ide do " + sklep.capitalize() + " i kupuje tu:" + str(zakupy.get(sklep)).title())
  print(f"{liczebniki.get(wizyta)} sklep to {sklep.capitalize()} i kupuje tu: {str((zakupy.get(sklep))).title()}")
  count = count + len(zakupy.get("piekarnia"))
  wizyta = wizyta + 1

print (f"Total zakupów: {count}")
count = 0
wizyta = 1
for sklep, produkt in zakupy.items():
  
  if liczebniki.get(wizyta) == None:
    nr_sklepu = "Kolejny"
  else:
    nr_sklepu = liczebniki.get(wizyta)

  print(f"{nr_sklepu} sklep to {sklep.capitalize()} i kupuje tu: {str(produkt).title()}")
  count = count + len(zakupy.get("piekarnia"))
  wizyta = wizyta + 1

print (f"Total zakupów: {count}")
