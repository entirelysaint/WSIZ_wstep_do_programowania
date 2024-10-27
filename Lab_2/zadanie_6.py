# Zadanie 6

litera = input("Podaj literę: ")

if len(litera) == 1:
    if litera.isupper():
        print("Litera jest duża")
    elif litera.islower():
        print("Litera jest mała")
    else:
        print("To nie jest litera")
else:
    print("Wprowadź jedną literę")