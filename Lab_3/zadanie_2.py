# Zadanie 2: Wyświetlanie pierwszych 10 liczb pierwszych
liczba = 2
liczby_pierwsze = []

while len(liczby_pierwsze) < 10:
    for i in range(2, liczba):
        if liczba % i == 0:
            break
    else:
        liczby_pierwsze.append(liczba)
    liczba += 1

print(",".join(map(str, liczby_pierwsze)))