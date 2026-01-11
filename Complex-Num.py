from math import sqrt

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.real == 0:
            return "{}i".format(self.imag)
        
        if self.imag == 0:
            return "{}".format(self.real)
        
        if self.imag < 0:
            return "{} - {}i".format(self.real, abs(self.imag))
        
        return "{} + {}i".format(self.real, self.imag)
    
    def _add_(self, other):
        a = self.real
        b = self.imag

        c = other.real
        d = other.imag
        return ComplexNumber(a + c, b + d)
    def _sub_(self, other):
        a = self.real
        b = self.imag

        c = other.real
        d = other.imag
        return ComplexNumber(a - c, b - d)
    def _mul_(self, other):
        a = self.real
        b = self.imag

        c = other.real
        d = other.imag
        return ComplexNumber(a * c - b * d, a * d + b * c)
    def _truediv_(self, other):
        a = self.real
        b = self.imag

        c = other.real
        d = other.imag
        denom = c**2 + d**2
        return ComplexNumber((a * c + b * d) / denom, (b * c - a * d) / denom)
    
a = ComplexNumber(3, 2)
b = ComplexNumber(1, 7)
print(a + b)  # Output: 4 + 9i
print(a - b)  # Output: 2 - 5i
print(a * b)  # Output: -11 + 23i
print(a / b)  # Output: 0.34 - 0.38i




    