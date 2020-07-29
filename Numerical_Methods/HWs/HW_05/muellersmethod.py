import math
import cmath


def mullersmethod(f, xnm2, xnm1, xn, epsilon):
    """
    @param f: parabolic function with real root
    @params xnm2, xnm1, xn: initial points to construct parabola
    @param epsilon: smallest distance between potential zero and actual zero
    """
    epsilon = 10**-7
    i = 0
    x_array = [xnm2, xnm1, xn]
    y_array = [f(xnm2), f(xnm1), f(xn)]
    while(abs(f(xn)) > epsilon):
    	q = (xn - xnm1)/(xnm1 - xnm2)
    	a = q*f(xn) - q*(1+q)*f(xnm1) + q**2*f(xnm2)
    	b = (2*q + 1)*f(xn) - (1+q)**2*f(xnm1) + q**2*f(xnm2)
    	c = (1 + q)*f(xn)
    	#see which x intercept is better
    	r = xn - (xn - xnm1)*((2*c)/(b + cmath.sqrt(b**2 - 4*a*c)))
    	s = xn - (xn - xnm1)*((2*c)/(b - cmath.sqrt(b**2 - 4*a*c)))
    	if(abs(f(r)) < abs(f(s))):
    		xplus = r
    	else:
    		xplus = s
    	if xplus.imag == 0j:#result is real number
    		xplus = xplus.real
    		x_array.append(xplus)
    		y_array.append(f(xplus))
    	xnm2 = xnm1
    	xnm1 = xn
    	xn = xplus
    	i = i + 1
    return xplus, x_array, y_array, i
f = lambda x: x**3 + 2*x**2 + 10*x - 20
root, x_values, y_values, iterations = mullersmethod(f, 0, 1, 2, 1e-17)




""" Plotting """
import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
blue = '#34c3eb'
SMALL_SIZE = 12
MEDIUM_SIZE = 15
BIGGER_SIZE = 20


plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)

plt.plot(np.linspace(-1, 3, 200), f(np.linspace(-1, 3, 200)), color=pink)
plt.hlines(0, -1, 3, color=gold)
plt.scatter(x_array, y_array, c=blue)
plt.title(r'$f(x) = x^3 + 2x^2 + 10x - 20$')
plt.ylabel('f (x)')
plt.xlabel('X')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/muellergraphic.png')

plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Numerical_Methods/HW_05/files/muellergraphic.png')
