


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



   
def squaring_algorithm(x,n):
    if n == 0:
        return 1
    elif n == 1:
            return x 
    else:
        prod = squaring_algorithm(x,n//2)
        result = prod*prod

        if n%2 ==1:
            result = result*x
    return result


def calculate_monomials(x1,n1):

    monomials = []

    for i in range(n1+1):
        monomial = squaring_algorithm(x1,i)
        if i>1:
            value = i*monomial
        elif i==1:
            value = x1
        elif i==0:
            value = 1
        
        monomials.append(value)
    return monomials 

def repeated_squaring(x,n):

    monomials = calculate_monomials(x,n)
    value_of_polynomial = 0

    for element in monomials:
        value_of_polynomial += element
    
    return value_of_polynomial

 