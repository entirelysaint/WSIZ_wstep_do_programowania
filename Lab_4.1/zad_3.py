
# Wczytaj i wyświetl dane od użytkownika
imie = input("Podaj imię: ")
print(f"Witaj {imie}")

wiek = int(input("Podaj wiek: "))
print(f"Twój wiek to: {wiek}")

imie_nazwisko = input("Podaj imię i nazwisko: ")
inicjaly = "".join([x[0].upper() for x in imie_nazwisko.split()])
print(f"Inicjały: {inicjaly}")

tekst = input("Podaj łańcuch: ")
print(tekst * 5)

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
print(f"Połączone łańcuchy: {lancuch1 + lancuch2}")

polowa1 = lancuch1[:len(lancuch1)//2]
polowa2 = lancuch2[len(lancuch2)//2:]
print(f"Połączenie połówek: {polowa1 + polowa2}")
