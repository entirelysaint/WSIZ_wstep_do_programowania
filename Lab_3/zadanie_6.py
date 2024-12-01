# Zadanie 6: Pętla nieskończona z wyjściem przy liczbie ujemnej
while True:
    try:
        liczba = int(input("Podaj liczbę całkowitą (podaj liczbę ujemną, aby zakończyć): "))
        if liczba < 0:
            print("Koniec programu.")
            break
        else:
            print(f"Wprowadziłeś liczbę: {liczba}")
    except ValueError:
        print("To nie jest liczba całkowita. Spróbuj ponownie.")