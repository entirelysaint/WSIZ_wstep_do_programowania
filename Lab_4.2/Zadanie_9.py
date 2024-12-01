
# Funkcja rekurencyjna obliczająca n-ty wyraz ciągu Fibonacciego
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Wywołanie funkcji
n = int(input("Podaj n: "))
print(f"{n}-ty wyraz ciągu Fibonacciego: {fibonacci(n)}")
