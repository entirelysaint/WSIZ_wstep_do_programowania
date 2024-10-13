### Zadanie 1

#### A) Operacje matematyczne:
| Działanie         | Wynik   | Typ    |
|-------------------|---------|--------|
| **1 + 2**         | 3       | `int`  |
| **1 + 4.5**       | 5.5     | `float`|
| **3 / 2**         | 1.5     | `float`|
| **4 / 2**         | 2.0     | `float`|
| **3 // 2**        | 1       | `int`  |
| **-3 // 2**       | -2      | `int`  |
| **11 % 2**        | 1       | `int`  |
| **2 ** 10**       | 1024    | `int`  |
| **8 ** (1/3)**    | 2.0     | `float`|

#### B) Działanie funkcji konwertujących:
| Funkcja           | Wynik   | Typ    |
|-------------------|---------|--------|
| **int(3.0)**      | 3       | `int`  |
| **float(3)**      | 3.0     | `float`|
| **float("3")**    | 3.0     | `float`|
| **str(12.4)**     | '12.4'  | `str`  |
| **bool(0)**       | False   | `bool` |

### Wyjaśnienie typów danych:

1. **`int` (integer)**:
   - Reprezentuje liczby całkowite (bez części dziesiętnej). Przykłady: `3`, `1024`, `-2`.  
   - Używany do przechowywania wartości liczbowych, które nie mają części ułamkowych.

2. **`float` (floating-point number)**:
   - Reprezentuje liczby zmiennoprzecinkowe, czyli liczby z częścią dziesiętną. Przykłady: `5.5`, `2.0`, `1.5`.  
   - Jest przydatny do przechowywania wyników operacji arytmetycznych z ułamkami lub obliczeń wymagających precyzji dziesiętnej.

3. **`str` (string)**:
   - Reprezentuje ciągi znaków, czyli tekst. Przykłady: `'12.4'`, `"hello"`, `"Python"`.  
   - Używany do przechowywania tekstu, numerów w formie nie numerycznej (np. numery telefonów), a także znaków specjalnych.

4. **`bool` (boolean)**:
   - Reprezentuje wartości logiczne: `True` (prawda) lub `False` (fałsz).  
   - Używany w logice programowania do reprezentowania warunków i wyników operacji logicznych, takich jak porównania (`==`, `>`, itp.) lub funkcje zwracające prawdę/fałsz.