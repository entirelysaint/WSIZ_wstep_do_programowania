# lab2_solutions.py
# Autor: Kacper Masiewicz
# Numer albumu: 72640
# Opis: Rozwiązania do zadań z Laboratorium nr 2

# Zadanie 1
# Program sprawdzający wynik egzaminu na podstawie zdobytych punktów
def zadanie_1(punkty):
    if punkty > 80:
        wynik = "Zaliczenie w terminie 0"
    elif 50 <= punkty <= 80:
        wynik = "Możliwość poprawy"
    else:
        wynik = "Konieczność poprawy"
    return wynik
# Przykład: zadanie_1(85) zwraca "Zaliczenie w terminie 0"

# Zadanie 2
# Program porządkujący trzy liczby x, y i z od najmniejszej do największej
def zadanie_2(x, y, z):
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    return x, y, z
# Przykład: zadanie_2(3, 1, 2) zwraca (1, 2, 3)

# Zadanie 3
# Program sprawdzający rozszerzenie pliku
def zadanie_3(nazwa_pliku):
    return "Tak" if nazwa_pliku.endswith('.xlsx') else "Nie"
# Przykład: zadanie_3("Raport_maj.xlsx") zwraca "Tak"

# Zadanie 4
# Program obliczający wynik drużyny piłkarskiej na podstawie liczby goli i bonusów
def zadanie_4(gol, bonus):
    wynik = gol * 10
    if gol > 10:
        wynik += 15
    elif gol > 5:
        wynik += 5
    wynik += bonus
    return wynik
# Przykład: zadanie_4(6, 10) zwraca 75

# Zadanie 5a
# Odczyt danych z pliku
def zadanie_5a():
    with open("notowania_gieldowe.txt", "r") as plik:
        for linia in plik:
            print(linia.strip())
# Przykład wywołania wypisuje każdą linię z pliku

# Zadanie 5b
# Dopisanie nowej spółki do pliku i ponowne odczytanie
def zadanie_5b():
    with open("notowania_gieldowe.txt", "a") as plik:
        plik.write("\nALR, 113")
    zadanie_5a()
# Przykład wywołania dodaje "ALR, 113" do pliku i wypisuje jego zawartość

# Zadanie 6
# Sprawdzenie, czy litera wprowadzona przez użytkownika jest duża czy mała
def zadanie_6(litera):
    return "Duża litera" if litera.isupper() else "Mała litera"
# Przykład: zadanie_6('A') zwraca "Duża litera"

# Zadanie 7
# Sprawdzenie poprawności hasła na podstawie długości i obecności znaku specjalnego
def zadanie_7(haslo):
    if len(haslo) == 11 and '!' in haslo:
        return "Hasło jest poprawne"
    else:
        return "Hasło jest niepoprawne"
# Przykład: zadanie_7('pk47!jy0893') zwraca "Hasło jest poprawne"

# Zadanie 8
# Wyodrębnienie części tekstu
def zadanie_8(text):
    pierwsze_trzy = text[:3]
    ostatnie_dwa = text[-2:]
    return pierwsze_trzy, ostatnie_dwa
# Przykład: zadanie_8('Studiuje-Informatykę') zwraca ('Stu', 'ę')

# Zadanie 9
# Zamiana dużych liter na małe i na odwrót
def zadanie_9(text):
    return text.swapcase()
# Przykład: zadanie_9('Studiuje-Informatykę') zwraca 'sTUDIJE-iNFORMATYKĘ'