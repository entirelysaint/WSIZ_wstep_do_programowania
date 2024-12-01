
# Funkcja obliczająca pole trójkąta za pomocą wzoru Herona
import math

def pole_trojkata(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        raise ValueError("Podane boki nie tworzą trójkąta")

# Wywołanie funkcji
try:
    a, b, c = map(float, input("Podaj boki trójkąta oddzielone spacją: ").split())
    print(f"Pole trójkąta wynosi: {pole_trojkata(a, b, c):.2f}")
except ValueError as e:
    print(f"Błąd: {e}")
