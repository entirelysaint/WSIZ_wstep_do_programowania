
# Funkcja o zmiennej liczbie parametrów
def wyswietl_parametry(*args):
    print("Podane parametry:", args)

def znajdz_maksimum(*args):
    return max(args) if args else None

# Wywołanie funkcji
wyswietl_parametry(1, 2, 3, 4)
print("Maksimum:", znajdz_maksimum(1, 2, 3, 4))
