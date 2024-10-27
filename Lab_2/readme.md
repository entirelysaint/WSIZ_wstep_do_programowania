# # Laboratorium 2 - Readme

## Wstęp do Programowania - mgr inż. Anna Marczakiewicz

### Tematyka:
* Instrukcja warunkowa `if`, `elif`, `else`
* Praca z plikami

### Opis:

Ten projekt zawiera rozwiązania zadań z Laboratorium 2 z przedmiotu "Wstęp do Programowania". Skrypt ten demonstruje zastosowanie instrukcji warunkowych oraz operacji na plikach w języku Python. 

### Zadania:

1. **Ocena z egzaminu:** Program pobiera od użytkownika liczbę punktów i wyświetla informację o wyniku egzaminu:
    * **> 80 punktów:** Egzamin zaliczony w terminie 0.
    * **50-80 punktów:** Możliwość poprawy.
    * **< 50 punktów:** Konieczność poprawy.

2. **Sortowanie trzech liczb:** Program sortuje trzy liczby wprowadzone przez użytkownika od najmniejszej do największej, bez użycia wbudowanych funkcji sortujących.

3. **Sprawdzanie rozszerzenia pliku:** Program sprawdza, czy zmienna `Nazwa_pliku` zawiera nazwę pliku z rozszerzeniem ".xlsx" i wyświetla odpowiedni komunikat.

4. **Obliczanie wyniku drużyny piłkarskiej:** Program oblicza całkowity wynik drużyny piłkarskiej na podstawie liczby zdobytych bramek (`gol`) i ewentualnych punktów bonusowych (`bonus`):
    * **a)** Punkty bonusowe są przyznawane oddzielnie za przekroczenie 5 i 10 bramek.
    * **b)** Punkty bonusowe za przekroczenie 5 i 10 bramek sumują się.

5. **Operacje na plikach:**
    * **a)** Program odczytuje plik `notwania_gieldowe.txt` i wyświetla jego zawartość.
    * **b)** Program dopisuje nową linię do pliku `notwania_gieldowe.txt` i ponownie wyświetla jego zawartość.

6. **Sprawdzanie wielkości liter:** Program sprawdza, czy litera wprowadzona przez użytkownika jest duża czy mała.

7. **Walidacja hasła:** Program sprawdza, czy zmienna `Hasło` spełnia następujące warunki:
    * Długość 11 znaków.
    * Zawiera znak specjalny '!'.

8. **Wycinanie znaków z ciągu:** Program wykorzystuje operator wycinania `[:]` do wyodrębnienia:
    * Pierwszych trzech znaków z ciągu `text`.
    * Ostatnich dwóch znaków z ciągu `text`.

9. **Zamiana wielkości liter:** Program zmienia wszystkie duże litery na małe i na odwrót w podanym ciągu znaków, wykorzystując metodę `swapcase()`.

### Uruchomienie:

Aby uruchomić skrypt, należy zapisać go w pliku `.py` i uruchomić z poziomu konsoli lub interpretera Pythona.