from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        divisor = gcd(self.numerator, self.denominator)
        self.numerator //= divisor
        self.denominator //= divisor

    def add(self, other):
        return Fraction(self.numerator * other.denominator + other  .numerator * self.denominator,self.denominator * other.denominator)

    def subtract(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def multiply(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def divide(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else str(self.numerator)

f1 = Fraction(3, 4)
f2 = Fraction(2, 5)

print(f"f1: {f1}")
print(f"f2: {f2}")
print(f"f1 + f2: {f1.add(f2)}")
print(f"f1 - f2: {f1.subtract(f2)}")
print(f"f1 * f2: {f1.multiply(f2)}")
print(f"f1 / f2: {f1.divide(f2)}")
