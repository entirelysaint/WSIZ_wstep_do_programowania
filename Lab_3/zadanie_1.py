# Zadanie 1: Kontrola zużycia paliwa w samolocie
paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Pozostało paliwa: {paliwo} litrów")
    paliwo -= paliwo_zużyte_na_s
    czas += 1
    if paliwo <= 0:
        print("Koniec lotu.")
        break