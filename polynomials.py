


def brute_force(x,n):
    p = 1

    for i in range(0,n+1):

        power = 1     
        for j in range(1,i+1):
                power = power * x


        p = p + (i*power) 
        
    
    return p 


def horners_rule(x,n):

    value = x*n

    for i in range(n,-1,-1):
        if i == n:
            value = value + i-1
        elif i == 0:
            value = value + 1
        else:
            value = value*x + i - 1
    
        return(value)


class Repeated_Square:
    
    def __init__(self,x,n):
        self.x = x
        self.n = n
    def __squaring_algorithm(self):
        x=self.x
        n=self.n
        if n == 0:
            return 1
        elif n == 1:
                return x 
        else:
            prod = self.__squaring_algorithm(x,n//2)
            result = prod*prod

            if n%2 ==1:
                result = result*x
        return result


    def __calculate_monomials(self):
        x = self.x
        n = self.n
        monomials = []

        for i in range(n+1):
            monomial = self.__squaring_algorithm(x,i)
            if i>1:
                value = i*monomial
            elif i==1:
                value = x
            elif i==0:
                value = 1
            
            monomials.append(value)
        return monomials 

    def calculate_polynomial(self):
        x = self.x
        n = self.n

        monomials = self.__calculate_monomials(x,n)
        value_of_polynomial = 0

        for element in monomials:
            value_of_polynomial += element
        
        return value_of_polynomial

 