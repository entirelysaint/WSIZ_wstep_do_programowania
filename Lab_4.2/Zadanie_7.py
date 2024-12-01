
# Funkcja rekurencyjna obliczająca potęgę
def potega(a, n):
    if n == 0:
        return 1
    return a * potega(a, n - 1)

# Wywołanie funkcji
a = float(input("Podaj podstawę: "))
n = int(input("Podaj wykładnik: "))
print(f"{a} do potęgi {n} wynosi: {potega(a, n)}")
