class Polynomial:
    
    # takes in list coeffs
    def __init__(self, coeffs):
        self._coeffs = coeffs
        
    def get_coeff(self):
        return self._coeffs
        
    # checks if polynomials are equal
    def __eq__(self, other):
        
        # removing leading zeros
        p1 = self._coeffs.copy()
        p2 = other._coeffs.copy()
        while p1 and p1[0] == 0:
            p1.pop(0)
        while p2 and p2[0] == 0:
            p2.pop(0)
        
        return p1 == p2
    
    # Challenge: prints the polynomial 
    def __str__(self):
        
        # case for 0
        if self._coeffs[0] == 0 and len(self._coeffs) == 1:
            return "0"
        
        poly_str = ''
        first_power = len(self._coeffs) - 1
        for i, coef in enumerate(self._coeffs):
            power = first_power - i
            if coef:
                if coef < 0:
                    sign = (' - ' if poly_str else '-')
                    coef = -coef
                elif coef > 0:
                    sign = (' + ' if poly_str else '')
                coef_str = '' if coef == 1 and power != 0 else str(coef)
                
                if power == 0:
                    power_str = ''
                elif power == 1:
                    power_str = 'x'
                else:
                    power_str = 'x^' + str(power)
                poly_str += sign + coef_str + power_str
        return poly_str
    
    # returns highest power of a variable
    def deg(self):
        p1 = self._coeffs.copy()
        # case: list empty
        if not self._coeffs:
            return -1
        while p1 and p1[0] == 0:
            p1.pop(0)
        return len(p1) - 1
    
    # returns the coefficient of x^i
    def coeff(self, i):
        if i == len(self._coeffs):
            return 0
        value = len(self._coeffs) - i - 1
        if value < 0:
            return 0
        return self._coeffs[value]
    
    # adding two polynomials together
    def __add__(self, other):
        
        max_len = max(len(self._coeffs), len(other._coeffs))
        num_zeros = abs(len(self._coeffs) - len(other._coeffs))
        
        p1 = self._coeffs.copy()
        p2 = other._coeffs.copy()
        
        if len(p1) > len(p2):
            p2 = [0] * num_zeros + p2
        else:
            p1 = [0] * num_zeros + p1
        
        result = [0] * max_len

        for i in range(len(p1)):
            result[i] += p1[i]

        for i in range(len(p2)):
            result[i] += p2[i]

        return Polynomial(result)
    
    # subtracting two polynomials
    def __sub__(self, other):
        
        # adding leading zeros
        max_len = max(len(self._coeffs), len(other._coeffs))
        num_zeros = abs(len(self._coeffs) - len(other._coeffs))
        
        p1 = self._coeffs.copy()
        p2 = other._coeffs.copy()
        
        if len(p1) > len(p2):
            p2 = [0] * num_zeros + p2
        else:
            p1 = [0] * num_zeros + p1
        
        result = [0] * max_len
        
        for i in range(max_len):
            result[i] = p1[i] - p2[i]
        
        return Polynomial(result)
    
    # multiplying two polynomials
    def __mul__(self, other):
        
        result_degree = (len(self._coeffs) - 1) + (len(other._coeffs) - 1)
        result = [0] * (result_degree + 1)
        
        p1 = self._coeffs.copy()
        p2 = other._coeffs.copy()
        
        for i in range(len(p1)):
            for j in range(len(p2)):
                result[i+j] += p1[i] * p2[j]
        while result and result[0] == 0:
            result.pop(0)       
        return Polynomial(result)
    
    # dividing two polynomials
    def poly_division(self, other):
        
        p1 = self._coeffs.copy()
        p2 = other._coeffs.copy()
        
        # removing leading zeros
        while p1 and p1[0] == 0:
            p1.pop(0)
        while p2 and p2[0] == 0:
            p2.pop(0)
        
        # after popping zeros, if zeros were the only element in list
        # the list should be empty
        if len(p2) == 0:
            raise ZeroDivisionError()
        
        dividend = p1.copy()
        divisor = p2.copy()
        quotient = [0] * (len(dividend) - len(divisor) + 1)
        counter = 0

        while len(dividend) >= len(divisor):
            term_factor = dividend[0] / divisor[0]
            
            for i in range(len(divisor)):
                dividend[i] -= term_factor * divisor[i]

            quotient[counter] = term_factor
            counter+=1
            
            while len(dividend) > 0 and dividend[0] == 0:
                dividend.pop(0)
        return Polynomial(quotient), Polynomial(dividend)
        
    # quotient of two polynomials | self = dividend | other = divisor
    def __floordiv__(self, other):
        quotient, remainder = self.poly_division(other)
        return quotient
    
    # remainder of two polynomials      
    def __mod__(self, other):
        quotient, remainder = self.poly_division(other)
        return remainder
    
    # evaluates the polynomial at a and return value
    def evaluate(self, a):
        length = len(self._coeffs)
        result = [0] * length
        for i in range(length):
            result[i] = self._coeffs[i] * (a**(length - i - 1))
        
        return sum(result)
    
                

        
        
        
        
