
# Funkcja obliczająca BMI
def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    if bmi < 18.5:
        kategoria = "niedowaga"
    elif 18.5 <= bmi < 25:
        kategoria = "pożądana masa ciała"
    elif 25 <= bmi < 30:
        kategoria = "nadwaga"
    else:
        kategoria = "otyłość"
    return bmi, kategoria

# Wywołanie funkcji
waga = float(input("Podaj wagę w kg: "))
wzrost = float(input("Podaj wzrost w metrach: "))
bmi, kategoria = oblicz_bmi(waga, wzrost)
print(f"Twoje BMI: {bmi:.2f}, Kategoria: {kategoria}")
