
# Operacje na krotce stopnie
stopnie = ("Szeregowy", "Kapral", "Sierżant", "Porucznik", "Kapitan", "Major", "Pułkownik")

ilosc_stopni = len(stopnie)
Major_index = stopnie.index("Major")
Pulawnik_wystepowanie = "Pułkownik" in stopnie

print("Liczba stopni:", ilosc_stopni)
print("Indeks 'Major':", Major_index)
print("Czy 'Pułkownik' występuje:", Pulawnik_wystepowanie)
