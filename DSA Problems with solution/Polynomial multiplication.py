# Function to display the given polynomial
def display_poly(poly):
    for val in range(len(poly)):
        print(poly[val], end="")

        if val != 0:
            print('x^', val, end="")
        if val !=  len(poly)-1:
            print(' + ', end= "")


# Function to multiply the different polynomials
def mulpoly(poly1, poly2, size1, size2):
    product= [0] * (size1 + size2 - 1)                      # Creating the list which only contain zeros

    for coeff1 in range(size1):                             # Taking the number from the first list of the coefficient

        for coeff2 in range(size2):                         # Taking the number from the first list of the coefficient

            product[coeff1+coeff2] += (poly1[coeff1] * poly2[coeff2])

    return product                                          # Time complexity of this function is O(n^2) which is too big and that why we are writing the effective
                                                            # Function to calculate the product of two polynomials.


# Function to add the different list or different polynomials
def add(poly1, poly2):
    add_on= [0] * max(len(poly1), len(poly2))
    if len(poly1) == 0:
        return poly2
    elif len(poly2) == 0:
        return poly1
    else:
        for i in range(len(add_on)):
            if i < len(poly1):
                add_on[i] += poly1[i]
            if i < len(poly2):
                add_on[i] += poly2[i]
    return add_on


# Function to subtract the different list or different polynomials
def sub(poly1, poly2):
    sub_out= [0] * max(len(poly1), len(poly2))
    if len(poly1) == 0:
        return poly2
    elif len(poly2) == 0:
        return poly1
    else:
        for i in range(len(sub_out)):
            if i < len(poly1):
                sub_out[i] += poly1[i]
            if i < len(poly2):
                sub_out[i] -= poly2[i]
    return sub_out


# Function to split the polynomial into two different halves
def split(poly1, poly2):
    n= max(len(poly1), len(poly2))
    mid= n // 2
    return (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])


# Function to increase the exponent of the numbers
def increase_expo(poly, n):
    return [0] * n + poly


# Function of effective polynomial multiplication
def eff_mulpoly(poly1, poly2):
    if len(poly1) == 1:
        return [poly1[0] * poly2[i] for i in range(len(poly2))]
    elif len(poly2) == 1:
        return [poly2[0] * poly1[i] for i in range(len(poly1))]
    else:
        n= max(len(poly1), len(poly2))

        a, b= split(poly1, poly2)
        y= eff_mulpoly(add(a[0], a[1]), add(b[0], b[1]))
        U= eff_mulpoly(a[0], b[0])
        Z= eff_mulpoly(a[1], b[1])

        Y= sub(y, add(U, Z))

        return add(U, add(increase_expo(Y, n//2), increase_expo(Z, n)))




poly1= [5, 0, 10, 6]
poly2= [1, 2, 4]
print('Polynomail 1: ')
display_poly(poly1)
print('\nPolynomail 2: ')
display_poly(poly2)
prod= eff_mulpoly(poly1, poly2)
print('\nProduct of both the polynomial: ')
display_poly(prod)
print(prod)
