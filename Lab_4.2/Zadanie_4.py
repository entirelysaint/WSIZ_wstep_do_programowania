
# Funkcja obliczająca średnią z listy liczb
def srednia(lista_liczb):
    return sum(lista_liczb) / len(lista_liczb) if lista_liczb else 0

# Wywołanie funkcji
liczby = [float(x) for x in input("Podaj liczby oddzielone spacją: ").split()]
print(f"Średnia wynosi: {srednia(liczby)}")
