
"""
Parameters: x, n 

Evaluates a polynomial of n degrees of the form 1 + x + ...+ n*x^n at the point, x, using the repeated squares method.

"""

class RepeatedSquare:
     
     def __init__(self):
          
          pass
     
     def squaring_algorithm(self,x,n):

        if n == 0:
            return 1
        elif n == 1:
                return x 
        else:
            prod = self.squaring_algorithm(x,n//2)
            result = prod*prod

            if n%2 ==1:
                result = result*x
        return result


     def calculate_monomials(self,x,n):

        monomials = []

        for i in range(n+1):
            monomial = self.squaring_algorithm(x,n)
            if i>1:
                value = i*monomial
            elif i==1:
                value = x
            elif i==0:
                value = 1
            
            monomials.append(value)
        return monomials 

     def calculate_polynomial(self,x,n):

        monomials = self.calculate_monomials(x,n)
        value_of_polynomial = 0

        for element in monomials:
            value_of_polynomial += element
        
        return value_of_polynomial




