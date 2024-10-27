# Zadanie 4

gol = int(input("Podaj liczbę bramek: "))
bonus = 0

# a)
if gol > 10:
    bonus += 10
if gol > 5:
    bonus += 5

wynik_a = gol * 10 + bonus
print(f"a) Całkowity wynik: {wynik_a}")

# b)
bonus = 0
if gol > 5:
    bonus += 5
if gol > 10:
    bonus += 10

wynik_b = gol * 10 + bonus
print(f"b) Całkowity wynik: {wynik_b}")