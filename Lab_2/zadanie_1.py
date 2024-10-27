# Zadanie 1

punkty = int(input("Podaj liczbę punktów: "))

if punkty > 80:
    print("Egzamin zaliczony w terminie 0")
elif punkty >= 50:
    print("Możesz poprawić wynik egzaminu")
else:
    print("Musisz poprawić wynik egzaminu")