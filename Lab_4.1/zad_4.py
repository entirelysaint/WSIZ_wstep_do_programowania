
# Wczytaj zdanie i przeanalizuj litery
zdanie = input("Podaj zdanie: ")
litery = sorted(set(filter(str.isalpha, zdanie.lower())))
print("Litery w kolejności alfabetycznej:", litery)

brakujace = [chr(x) for x in range(97, 123) if chr(x) not in litery]
print("Brakujące litery alfabetu:", brakujace)
