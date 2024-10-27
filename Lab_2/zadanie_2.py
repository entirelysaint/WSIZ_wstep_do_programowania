# Zadanie 2

x = int(input("Podaj liczbę x: "))
y = int(input("Podaj liczbę y: "))
z = int(input("Podaj liczbę z: "))

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print(f"Liczby w kolejności rosnącej: {x}, {y}, {z}")