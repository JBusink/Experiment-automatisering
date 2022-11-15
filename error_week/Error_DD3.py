class Polynomial:
    """A class used to represent a polynomial"""
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def get_derivative(self):
        """Calculate the first derivative of the polynomial"""
        new_coefficients = [(i+1) * self.coefficients[i+1] for i in range(len(self.coefficients) - 1)]
        return Polynomial(new_coefficients)

    def get_nth_derivative(self,n):
        """Calculate the nth derivative of the polynomial"""
        new_polynomial = self
        for i in range(n):
            new_polynomial = new_polynomial.get_derivative()
        return new_polynomial
    
    def __add__(self, other):
        """Dunder method for adding two polynomials"""
        new_coefficients = [self.coeffienciens[i] + other.coefficients[j] for i,j in zip(self.coefficients, other.coefficients)]
        return Polynomial(new_coefficients)

    def __repr__(self):
        """Representation of polynomial when printed"""
        return " + ".join([str(self.coefficients[i]) + f"x^{i}" for i in range(len(self.coefficients))])

polynomial = Polynomial([3, 2, 1])
second_derivative = polynomial.get_nth_derivative(2)

print(polynomial)
print(second_derivative)