def oblicz(liczba1, liczba2):
    suma = liczba1 + liczba2
    różnica = liczba1 - liczba2
    return suma, różnica
print(oblicz(22,13))
x, y = oblicz(4.14, 8.4)
print(f"Suma = {x} Różnica = {y}")