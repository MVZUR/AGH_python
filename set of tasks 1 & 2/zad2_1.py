class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real  # Część rzeczywista
        self.imag = imag  # Część urojona

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        raise TypeError("Dodawanie wymaga liczby zespolonej jako argumentu")

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        raise TypeError("Odejmowanie wymaga liczby zespolonej jako argumentu")

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"


# Przykład użycia
z1 = ComplexNumber(3, 4)
z2 = ComplexNumber(1, -2)

print("z1 =", z1)  # Wyświetl wartość z1
print("z2 =", z2)  # Wyświetl wartość z2

z3 = z1 + z2
print("z1 + z2 =", z3)  # Wyświetl wynik operacji z1 + z2

z4 = z1 - z2
print("z1 - z2 =", z4)  # Wyświetl wynik operacji z1 - z2
