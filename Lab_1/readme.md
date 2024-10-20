# Wstęp do programowania - Laboratorium 1

**Imię i nazwisko:** Kacper Masiewicz  
**Numer Albumu:** w72640  

## Opis projektu

Projekt zawiera rozwiązania zadań z **Laboratorium 1** przedmiotu **Wstęp do programowania**. Zadania te obejmują podstawy programowania w języku Python, takie jak operacje arytmetyczne, typy danych, instrukcje warunkowe, pętle, obliczenia matematyczne oraz wprowadzanie i wyświetlanie danych. Projekt został stworzony w środowisku **PyCharm** z wykorzystaniem wersji **Python 3.12**.

## Struktura pliku

Cały kod znajduje się w jednym pliku `zadania_lab1.py`. Każde zadanie jest poprzedzone komentarzem, który wyjaśnia, co robi kod, oraz zakończone komentarzem z wynikiem działania.

## Spis zadań

### Zadanie 1: Operacje arytmetyczne i typy danych
Sprawdzamy wynik i typ różnych operacji arytmetycznych oraz wyjaśniamy, jak działają operatory takie jak dodawanie, dzielenie, potęgowanie oraz reszta z dzielenia. Dodatkowo testujemy konwersję typów danych, takich jak `int`, `float`, `str` i `bool`.

### Zadanie 2: Przypisanie i wyświetlenie tekstu
Do zmiennej `uczelnia` przypisywany jest tekst **"Studiuję na WSIiZ"**, który następnie zostaje wyświetlony w konsoli.

### Zadanie 3: Wyświetlanie danych o osobie
Wyświetlamy informacje o osobie na podstawie zmiennych: `imię`, `wiek`, `wzrost`. Tekst zawiera informacje w formacie:  
*Nazywam się Jan i mam 20 lat. Mój wzrost to 178 cm.*

### Zadanie 4: Obliczenie ceny po rabacie
Obliczamy cenę produktu po zastosowaniu 20% rabatu. Wynik jest wyświetlany z dokładnością do dwóch miejsc po przecinku.

### Zadanie 5: Obliczanie pola i obwodu prostokąta
Skrypt pobiera od użytkownika długości boków prostokąta, a następnie oblicza i wyświetla jego pole oraz obwód.

### Zadanie 6: Zużycie paliwa i koszt podróży
Program pobiera od użytkownika dane dotyczące długości trasy, średniego spalania oraz ceny paliwa. Na tej podstawie oblicza i wyświetla zużycie paliwa oraz szacowane koszty podróży.

#### Zadanie 6A: Losowanie długości trasy
Modyfikacja zadania 6, w której długość trasy jest generowana losowo z zakresu 50-500 km, a użytkownik podaje cenę paliwa.

### Zadanie 7: Równanie liniowe
Rozwiązujemy równanie liniowe w postaci **ax + b = 0** na podstawie współczynników `a` i `b` podanych przez użytkownika.

### Zadanie 8: Równanie kwadratowe
Program rozwiązuje równanie kwadratowe **ax² + bx + c = 0**, obliczając deltę i wyznaczając jedno lub dwa rozwiązania (lub brak rozwiązań rzeczywistych), w zależności od wartości delty.

### Zadanie 9: Kalkulator
Kalkulator wykonujący operacje arytmetyczne (dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie) na dwóch liczbach podanych przez użytkownika.

## Wymagania

Do uruchomienia projektu potrzebujesz:
- **Python 3.12** lub nowszy
- Środowisko programistyczne, takie jak **PyCharm** (opcjonalnie)

## Instrukcje uruchomienia

1. Zainstaluj **Python**:  
   Pobierz i zainstaluj najnowszą wersję Pythona z [python.org](https://www.python.org/downloads/). Pamiętaj, aby podczas instalacji zaznaczyć opcję **Add Python to PATH**.
   
2. Otwórz projekt w **PyCharm**:  
   Jeśli chcesz użyć PyCharm, pobierz **PyCharm Community Edition** z [jetbrains.com](https://www.jetbrains.com/pycharm/).

3. Uruchom skrypt `zadania_lab1.py`:  
   Wykorzystaj dowolne narzędzie do uruchomienia skryptu (np. PyCharm, Visual Studio Code lub terminal).

## Przykład działania
Zadanie 5: Podaj długość boku A prostokąta: 5 Podaj długość boku B prostokąta: 10 Pole prostokąta: 50.0 Obwód prostokąta: 30.0


## Dodatkowe informacje

Skrypt zawiera także funkcje losowe oraz obsługę równań liniowych i kwadratowych. Zawiera interaktywne polecenia dla użytkownika, które wymagają podania odpowiednich wartości w trakcie działania programu.