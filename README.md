# Polynomial Operations

This Python program provides a class `Polynomial` for working with polynomials and a subclass `Quadratic` specifically for quadratic polynomials. It allows users to perform various operations such as addition, subtraction, multiplication, division, evaluation, and factoring on polynomials.

## Features

- **Polynomial Class**: The `Polynomial` class represents a polynomial and includes methods for polynomial operations.
  - **Constructor**: The constructor initializes a polynomial with a list of coefficients.
  - **Equality Check**: The `__eq__()` method checks if two polynomials are equal.
  - **String Representation**: The `__str__()` method converts the polynomial to a human-readable string.
  - **Degree Calculation**: The `deg()` method returns the degree of the polynomial.
  - **Coefficient Access**: The `coeff()` method retrieves the coefficient of a specific term.
  - **Arithmetic Operations**: The class supports addition, subtraction, multiplication, division, and modulo operations on polynomials.
  - **Evaluation**: The `evaluate()` method evaluates the polynomial at a given value.
  
- **Quadratic Class**: The `Quadratic` class inherits from `Polynomial` and provides additional functionalities for quadratic polynomials.
  - **Constructor**: Ensures that the polynomial has a degree of 2 and raises a `ValueError` if not.
  - **Discriminant Calculation**: The `discriminant()` method calculates the discriminant of the quadratic polynomial.
  - **Real Roots**: The `real_roots()` method returns the real roots of the quadratic polynomial.
  - **Factoring**: The `factors()` method factors the quadratic polynomial into linear polynomials.

## Usage

To use this program, you can import the `Polynomial` and `Quadratic` classes into your Python script:

```python
from polynomial import Polynomial
from quadratic import Quadratic
```
Then, you can create polynomial objects and perform various operations as demonstrated in the provided code.

## Testing
The program includes test cases to ensure the correctness of its functionalities. You can run these tests to verify the behavior of the implemented methods.

## Contribution
Contributions to this project are welcome! Feel free to submit issues or pull requests to suggest improvements or report bugs.
