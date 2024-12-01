# Zadanie 4: Średnia cena potraw i rachunek na osobę
liczba_dan = int(input("Podaj liczbę zamówionych potraw: "))
liczba_gosci = int(input("Podaj liczbę gości: "))

suma = 0
for _ in range(liczba_dan):
    cena = float(input("Podaj cenę potrawy: "))
    suma += cena

srednia_cena = suma / liczba_dan
rachunek_na_osobe = suma / liczba_gosci

print(f"Średnia cena potrawy: {srednia_cena:.2f}")
print(f"Rachunek na osobę: {rachunek_na_osobe:.2f}")