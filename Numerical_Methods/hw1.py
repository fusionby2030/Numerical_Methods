import numpy as np



#arctan 1 = pi/4

#String of arctan 1 for 8 sig digits

#print(np.format_float_positional(np.pi /4, precision=8))

def f(x, n):
    array = []
    for i in range(1, n+1):
        approx = ((-1.0)**(i-1))*((x**(2*i-1))/(2*i-1))
        array.append(approx)
    #print(array)
    return np.sum(array)
y = np.pi/4
y_prime = np.format_float_positional(np.pi /4, precision=6)

term = 1
print(y_prime)
print(f(1, 127324))

"""
Something to do with error propogation
"""
"""
while term < 10:
    approximation = f(1, term)
    significant = np.format_float_positional(approximation, precision=8)
    print(term, significant)
    if significant == true_value:
        print(term)
        #print("Juuhuu")
        break
    else:
        term += 1
"""
