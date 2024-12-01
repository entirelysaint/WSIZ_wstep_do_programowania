
# Utwórz listę i przetestuj operacje na listach
Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

# Przykłady operacji
print("Lista:", Moja_lista)
print("Długość listy:", len(Moja_lista))
print("Maksymalny element:", max(Moja_lista))
print("Minimalny element:", min(Moja_lista))
print("Suma elementów:", sum(Moja_lista))
print("Lista posortowana:", sorted(Moja_lista))

# Operacje modyfikujące listę
Moja_lista.append(100)
print("Dodanie elementu:", Moja_lista)
Moja_lista.insert(2, 50)
print("Dodanie na indeksie 2:", Moja_lista)
Moja_lista.pop()
print("Usunięcie ostatniego elementu:", Moja_lista)
Moja_lista.reverse()
print("Odwrócenie listy:", Moja_lista)
