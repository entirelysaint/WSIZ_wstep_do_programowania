
# Lista z imionami
imiona = ["Anna", "Kamil", "Zofia", "Jan"]
print("Posortowana lista:", sorted(imiona))
imiona.append("Piotr")
imiona.append("Marta")
print("Dodane osoby:", imiona)
print("Usunięta ostatnia osoba:", imiona.pop())
imiona.insert(3, "Tomasz")
print("Dodanie osoby na indeksie 3:", imiona)
imiona.reverse()
imiona *= 2
print("Odwrócona i zdublowana lista:", imiona)
