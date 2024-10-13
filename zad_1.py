# A) Sprawdzanie typów wyników działań
operations = [
    ('1 + 2', 1 + 2),
    ('1 + 4.5', 1 + 4.5),
    ('3 / 2', 3 / 2),
    ('4 / 2', 4 / 2),
    ('3 // 2', 3 // 2),
    ('-3 // 2', -3 // 2),
    ('11 % 2', 11 % 2),
    ('2 ** 10', 2 ** 10),
    ('8 ** (1/3)', 8 ** (1/3))
]

# Wyświetlanie wyników operacji i ich typów
for operation, result in operations:
    print(f"{operation} = {result}, typ: {type(result)}")

print("\n")

# B) Sprawdzanie typów dla konwersji danych
conversions = [
    ('int(3.0)', int(3.0)),
    ('float(3)', float(3)),
    ('float("3")', float("3")),
    ('str(12.4)', str(12.4)),
    ('bool(0)', bool(0))
]

# Wyświetlanie wyników konwersji i ich typów
for conversion, result in conversions:
    print(f"{conversion} = {result}, typ: {type(result)}")