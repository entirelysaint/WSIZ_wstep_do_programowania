# Zadanie 1: Typy danych i operatory
# Sprawdzenie typu wyników określonych działań i wyjaśnienie operatorów

print("Zadanie 1 - A:")
print(type(1 + 2))        # Dodawanie dwóch liczb całkowitych
print(type(1 + 4.5))      # Dodawanie liczby całkowitej i zmiennoprzecinkowej
print(type(3 / 2))        # Dzielenie zmiennoprzecinkowe
print(type(4 / 2))        # Dzielenie zmiennoprzecinkowe
print(type(3 // 2))       # Dzielenie całkowite
print(type(-3 // 2))      # Dzielenie całkowite z liczbą ujemną
print(type(11 % 2))       # Reszta z dzielenia
print(type(2 ** 10))      # Potęgowanie
print(type(8 ** (1/3)))   # Pierwiastkowanie

# Wynikiem operacji są typy danych jak: int, float.
# Operator // zwraca wynik dzielenia bez reszty, ** wykonuje potęgowanie, a % zwraca resztę z dzielenia.

# B) Sprawdzenie działania rzutowania typów
print("Zadanie 1 - B:")
print(int(3.0))      # Zmiana typu float na int
print(float(3))      # Zmiana typu int na float
print(float("3"))    # Zmiana string na float
print(str(12.4))     # Zmiana float na string
print(bool(0))       # Zmiana liczby na boolean (False dla 0)

# Wynikiem działania powyższych funkcji są odpowiednio int, float, str i bool.

# Zadanie 2: Przypisanie wartości do zmiennej i wyświetlenie jej
uczelnia = "Studiuję na WSIiZ"
print("\nZadanie 2:")
print(uczelnia)

# Wynik: Wyświetla tekst "Studiuję na WSIiZ".

# Zadanie 3: Wyświetlenie danych o osobie
imię = 'Jan'
wiek = 20
wzrost = 178

print("\nZadanie 3:")
print(f"Nazywam się {imię} i mam {wiek} lat.")
print(f"Mój wzrost to {wzrost} cm.")

# Wynik: Nazywam się Jan i mam 20 lat. Mój wzrost to 178 cm.

# Zadanie 4: Obliczenie ceny po rabacie
cena = 39.99
rabat = 0.2
cena_po_rabacie = cena * (1 - rabat)

print("\nZadanie 4:")
print(f"Cena po rabacie: {cena_po_rabacie:.2f} PLN")

# Wynik: Cena po rabacie to 31.99 PLN.

# Zadanie 5: Obliczenie pola i obwodu prostokąta
print("\nZadanie 5:")
bok_a = float(input("Podaj długość boku A prostokąta: "))
bok_b = float(input("Podaj długość boku B prostokąta: "))
pole = bok_a * bok_b
obwód = 2 * (bok_a + bok_b)

print(f"Pole prostokąta: {pole}")
print(f"Obwód prostokąta: {obwód}")

# Wynik: Skrypt oblicza pole i obwód prostokąta na podstawie długości podanych przez użytkownika.

# Zadanie 6: Obliczanie zużycia paliwa i kosztów podróży
print("\nZadanie 6:")
droga = float(input("Podaj liczbę kilometrów: "))
spalanie_na_100_km = float(input("Podaj średnie spalanie na 100 km: "))
cena_paliwa = float(input("Podaj cenę paliwa za litr: "))
zużycie_paliwa = droga * spalanie_na_100_km / 100
koszt = zużycie_paliwa * cena_paliwa

print(f"Zużycie paliwa: {zużycie_paliwa:.2f} litry")
print(f"Koszt podróży: {koszt:.2f} PLN")

# Wynik: Program wylicza zużycie paliwa i koszt podróży na podstawie drogi, spalania i ceny paliwa.

# Zadanie 6A: Losowanie drogi i pobieranie ceny paliwa
import random

print("\nZadanie 6A:")
droga = random.randint(50, 500)  # Losowanie drogi z zakresu 50-500 km
print(f"Losowa droga: {droga} km")
spalanie_na_100_km = float(input("Podaj średnie spalanie na 100 km: "))
cena_paliwa = float(input("Podaj cenę paliwa za litr: "))
zużycie_paliwa = droga * spalanie_na_100_km / 100
koszt = zużycie_paliwa * cena_paliwa

print(f"Zużycie paliwa: {zużycie_paliwa:.2f} litry")
print(f"Koszt podróży: {koszt:.2f} PLN")

# Wynik: Program losuje drogę, a użytkownik podaje cenę paliwa.

# Zadanie 7: Rozwiązywanie równania liniowego ax + b = 0
print("\nZadanie 7:")
a = float(input("Podaj wartość współczynnika a: "))
b = float(input("Podaj wartość współczynnika b: "))
if a != 0:
    x = -b / a
    print(f"Rozwiązanie równania: x = {x}")
else:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań.")
    else:
        print("Równanie nie ma rozwiązań.")

# Wynik: Program rozwiązuje równanie liniowe w zależności od wartości a i b.

# Zadanie 8: Rozwiązywanie równania kwadratowego ax^2 + bx + c = 0
import math

print("\nZadanie 8:")
a = float(input("Podaj wartość współczynnika a: "))
b = float(input("Podaj wartość współczynnika b: "))
c = float(input("Podaj wartość współczynnika c: "))
delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(f"Równanie ma dwa rozwiązania: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"Równanie ma jedno rozwiązanie: x = {x}")
else:
    print("Równanie nie ma rozwiązań rzeczywistych.")

# Wynik: Program oblicza deltę i rozwiązuje równanie kwadratowe.

# Zadanie 9: Kalkulator dla dwóch liczb
print("\nZadanie 9:")
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

print(f"Dodawanie: {liczba1 + liczba2}")
print(f"Odejmowanie: {liczba1 - liczba2}")
print(f"Mnożenie: {liczba1 * liczba2}")
print(f"Dzielenie: {liczba1 / liczba2}")
print(f"Potęgowanie: {liczba1 ** liczba2}")

# Wynik: Program wykonuje operacje arytmetyczne dla dwóch podanych przez użytkownika liczb.