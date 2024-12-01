
# Funkcja zwracająca wspólne wartości dla dwóch sekwencji
def wspolne_wartosci(seq1, seq2):
    return list(set(seq1) & set(seq2))

# Wywołanie funkcji
seq1 = input("Podaj pierwszą sekwencję (elementy oddzielone spacją): ").split()
seq2 = input("Podaj drugą sekwencję (elementy oddzielone spacją): ").split()
print("Wspólne wartości:", wspolne_wartosci(seq1, seq2))
