# Zadanie 7: Średnia liczba punktów w grupie

# Wersja z pętlą warunkową:
n = int(input("Podaj liczbę studentów: "))
suma_punktow = 0
liczba_studentow = 0

while liczba_studentow < n:
    punkty = int(input("Podaj liczbę punktów: "))
    if punkty < 0 or punkty > 100:
        continue
    suma_punktow += punkty
    liczba_studentow += 1

print(f"Średnia punktów: {suma_punktow / n:.2f}")


# Wersja z pętlą nieskończoną:
suma_punktow = 0
liczba_studentow = 0

while True:
    punkty = int(input("Podaj liczbę punktów: "))
    if punkty < 0:
        break
    if punkty > 100:
        continue
    suma_punktow += punkty
    liczba_studentow += 1

if liczba_studentow > 0:
    print(f"Średnia punktów: {suma_punktow / liczba_studentow:.2f}")
else:
    print("Nie wprowadzono prawidłowych danych.")