# Name: Kan Xing Zheng
# Collaborators: 
# Notes: Challenge attempted

from polynomial import Polynomial
from math import sqrt

class Quadratic(Polynomial):
    
    def __init__(self, coeffs):
        if len(coeffs) != 3:
            raise ValueError
        if coeffs[0] == 0:
            raise ValueError
        Polynomial.__init__(self, coeffs)
    
    def discriminant(self):
        a = self._coeffs[0]
        b = self._coeffs[1]
        c = self._coeffs[2]
        
        return (b**2) - 4 * (a * c)
    
    def real_roots(self):
        roots = []
        discrim = self.discriminant()
        
        if discrim < 0:
            return roots
        
        sqrt_discrim = sqrt(discrim)
        a = self._coeffs[0]
        b = self._coeffs[1]
        r1 = (-b + sqrt_discrim) / (2 * a)
        r2 = (-b - sqrt_discrim) / (2 * a)
        if r1 < r2:
            roots.append(r1)
            roots.append(r2)
        else:
            roots.append(r2)
            roots.append(r1)
        return roots
    
    
    # Challenge: factors, both factors have integer coefficients
    def factors(self):
        roots = self.real_roots()
        a = self._coeffs[0]
        b = 1
        
        # cannot be factored
        if len(roots) == 0:
            return [self]
        
        r = -roots[0] * a
        s = -roots[1]
        
        if a != 1:     
            int_s = int(s)  
            if int_s != s:
                a = a / 2
                r = r / 2
                b = b * 2
                s = s * 2

        p1 = Polynomial([a, r])
        p2 = Polynomial([b, s])
        return [p1, p2]
        
        
        
