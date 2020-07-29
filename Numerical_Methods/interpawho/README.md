# Interpolation

## Lagrange Interpolation
The quation for lagrange interpolation starts with ![Lagrange Equation](images/lagrange_equation.png) which uses the polynomial described by ![Lagrange Polynomial](images/lagrange_polynomials.png). So we basically make n different polynomials and add them together to interpolate the input data set.

One makes also use of the Tschebyscheff nodes from the equation ![cheb roots](images/cheb_roots.png) to help counter act the random oscillations that come with evenly spaced points along an interval.


## Newton's Divided Difference
Newton's method uses the basis polynomials ![Newt Basis Poly](images/newton_basis_poly.png) which have coefficients determined by divided differences ![Newt Table](images/newtonTable.png)

## Splines
For splines, we create n -1 different polynomials that are differential at the n points such that they are continuous. ![Splines](images/splines_equation.png)
