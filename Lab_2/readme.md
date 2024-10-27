# Laboratorium 2 - Rozwiązania

**Autor:** Kacper Masiewicz  
**Numer albumu:** 72640  

## Opis Projektu
Projekt zawiera rozwiązania zadań z laboratorium nr 2, realizowanego w ramach przedmiotu *Wstęp do Programowania*. Skrypt `lab2_solutions.py` demonstruje wykorzystanie instrukcji warunkowych, operacji na plikach oraz manipulacji tekstowych w Pythonie, zgodnie z zasadami obowiązującymi w programowaniu strukturalnym.

Każde zadanie jest zaprojektowane zgodnie z poleceniami, a wyniki są opisane komentarzami w kodzie. Do zadania 5 wymagana jest obecność pliku `notowania_gieldowe.txt`.

## Pliki Projektu
- **`lab2_solutions.py`** - Główny skrypt zawierający rozwiązania wszystkich zadań.
- **`notowania_gieldowe.txt`** - Plik tekstowy z przykładowymi danymi giełdowymi do zadań 5a i 5b.
- **`README.md`** - Dokumentacja projektu z instrukcjami oraz opisem zadań.

## Utworzenie Pliku `notowania_gieldowe.txt`
Plik `notowania_gieldowe.txt` jest używany w zadaniach 5a i 5b do wczytywania oraz dopisywania danych giełdowych. Każda linia zawiera nazwę spółki oraz jej wartość, oddzielone przecinkiem. Możesz samodzielnie utworzyć plik o tej zawartości:

```plaintext
ABC, 123
XYZ, 456
PQR, 789
KLM, 321
MNO, 654```

Alternatywnie, uruchomienie funkcji create_notowania_file() w skrypcie lab2_solutions.py automatycznie wygeneruje plik z powyższą zawartością.

Opis Zadań i Przykłady Wyników

# Zadanie 1

Opis: Program sprawdza wynik egzaminu na podstawie liczby zdobytych punktów.

	•	Warunki:
	•	Powyżej 80 punktów – zaliczenie w terminie 0.
	•	Od 50 do 80 punktów – możliwość poprawy.
	•	Poniżej 50 punktów – konieczność poprawy.
	•	Przykład:

```zadanie_1(85)  # Wynik: "Zaliczenie w terminie 0"```



# Zadanie 2

Opis: Program sortuje trzy liczby w kolejności od najmniejszej do największej, bez użycia funkcji wbudowanych.

	•	Przykład:

```zadanie_2(3, 1, 2)  # Wynik: (1, 2, 3)```



# Zadanie 3

Opis: Program sprawdza, czy podana nazwa pliku kończy się na .xlsx.

	•	Przykład:

```zadanie_3("Raport_maj.xlsx")  # Wynik: "Tak"```



# Zadanie 4

Opis: Oblicza wynik drużyny piłkarskiej na podstawie liczby goli i bonusów.

	•	Zasady:
	•	Każda bramka to 10 punktów.
	•	Powyżej 5 goli – dodatkowe 5 punktów bonusowych.
	•	Powyżej 10 goli – dodatkowe 10 punktów bonusowych (łącznie 15).
	•	Przykład:

```zadanie_4(6, 10)  # Wynik: 75```



# Zadanie 5a

Opis: Odczytuje i wypisuje zawartość pliku notowania_gieldowe.txt.

	•	Przykład Wywołania:

```zadanie_5a()  
# Wynik:
# ABC, 123
# XYZ, 456
# PQR, 789
# KLM, 321
# MNO, 654```



# Zadanie 5b

Opis: Dodaje nową linię do pliku notowania_gieldowe.txt i wypisuje jego zawartość.

	•	Przykład Wywołania:

```zadanie_5b()  
# Wynik:
# ABC, 123
# XYZ, 456
# PQR, 789
# KLM, 321
# MNO, 654
# ALR, 113```



# Zadanie 6

Opis: Sprawdza, czy wprowadzona litera jest duża czy mała.

	•	Przykład:

```zadanie_6('A')  # Wynik: "Duża litera"```



# Zadanie 7

Opis: Waliduje hasło pod kątem długości oraz obecności znaku specjalnego !.

	•	Przykład:

```zadanie_7('pk47!jy0893')  # Wynik: "Hasło jest poprawne"```



# Zadanie 8

Opis: Wyodrębnia z ciągu pierwsze trzy i ostatnie dwa znaki.

	•	Przykład:

```zadanie_8('Studiuje-Informatykę')  # Wynik: ('Stu', 'ę')```



# Zadanie 9

Opis: Zamienia duże litery na małe i odwrotnie.

	•	Przykład:

```zadanie_9('Studiuje-Informatykę')  # Wynik: 'sTUDIJE-iNFORMATYKĘ'```



## Uruchamianie Zadań

	1.	Skopiuj wszystkie pliki do jednego katalogu.
	2.	Upewnij się, że plik notowania_gieldowe.txt znajduje się w katalogu głównym.
	3.	Uruchom funkcje, importując lab2_solutions.py w terminalu.

## Przykładowe Wywołanie

```python from lab2_solutions import zadanie_1, zadanie_2, zadanie_3, zadanie_4, zadanie_5a, zadanie_5b, zadanie_6, zadanie_7, zadanie_8, zadanie_9```

print(zadanie_1(85))
print(zadanie_2(3, 1, 2))
print(zadanie_3("Raport_maj.xlsx"))
print(zadanie_4(6, 10))
zadanie_5a()
zadanie_5b()
print(zadanie_6('A'))
print(zadanie_7('pk47!jy0893'))
print(zadanie_8('Studiuje-Informatykę'))
print(zadanie_9('Studiuje-Informatykę'))

## Informacje dodatkowe

> Ten projekt ma na celu praktykę programowania z użyciem instrukcji warunkowych, operacji na plikach oraz operacji tekstowych w Pythonie. Każde zadanie jest samodzielnym ćwiczeniem, które można uruchomić i testować oddzielnie.
