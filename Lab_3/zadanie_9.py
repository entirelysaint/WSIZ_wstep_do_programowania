# Zadanie 9: Różne operacje na wejściu użytkownika
# Imię
imie = input("Podaj swoje imię: ")
print(f"Witaj, {imie}")

# Wiek
wiek = int(input("Podaj swój wiek: "))
print(f"Twój wiek to: {wiek}")

# Inicjały
imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
print(f"Twoje inicjały to: {imie[0]}.{nazwisko[0]}.")

# Powtarzanie łańcucha
tekst = input("Podaj jakiś tekst: ")
print(tekst * 5)

# Łączenie łańcuchów
tekst1 = input("Podaj pierwszy łańcuch: ")
tekst2 = input("Podaj drugi łańcuch: ")
print(f"Połączone: {tekst1 + tekst2}")

# Połowa łańcucha
tekst1 = input("Podaj pierwszy łańcuch: ")
tekst2 = input("Podaj drugi łańcuch: ")
print(f"Pierwsza połowa: {tekst1[:len(tekst1)//2] + tekst2[:len(tekst2)//2]}")