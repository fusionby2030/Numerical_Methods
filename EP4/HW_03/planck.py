import numpy as np
import matplotlib.pyplot as plt
#average N
#E_0 = hbar * w

def peq(x):
    return( x**5/np.exp(x)-1 )

def dpeq(x):
    return( x**4 * ((5-x)*np.exp(x)-5) / (np.exp(x)-1)**2 )

def d2peq(x):
  return( 20*x**3/(np.exp(x)-1) - 10*x**4*np.exp(x)/(np.exp(x)-1)**2 + 2*np.exp(2*x)*x**5/(np.exp(x)-1)**3 - np.exp(x)*x**5/(np.exp(x)-1)**2 )


wavelength_range = np.arange(0.01, 20, 0.01)


""" NEWTONS METHOD """
def newton(f,Df,x0,epsilon,max_iter):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f,Df,1,1e-8,10)
    Found solution after 5 iterations.
    1.618033988749989
    '''
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

approx = newton(dpeq, d2peq, 4, 1e-10, 10)
print(approx)

plt.plot(wavelength_range, peq(wavelength_range))
plt.plot(wavelength_range, dpeq(wavelength_range))
#plt.plot(wavelength_range, d2peq(wavelength_range))
plt.axvline(approx, label='root = {}'.format(approx), color='green')
plt.plot(wavelength_range, 0*wavelength_range, 'k--')
plt.legend(['u(x)', 'du/dx', 'du/dx = 0 when x = {}'.format(approx)])
plt.show()
