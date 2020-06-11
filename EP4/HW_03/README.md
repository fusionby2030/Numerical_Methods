# HW_02

## Problems

1.  Using  the  Planck  equation  determine  the  average  number  of  photons n per unit volume in a cavity with equilibrium radiation at temperature T.
2.  Using the Planck equation determine the average kinetic energy of a photon in a cavity with equilibrium radiation at temperature T.

3.  Using the Planck equation determine the coefficient b in the Wien’s displacement  law  written  for  the  maximum  of  the  spectral  energy  density u_λ,
namely λ_max*T = b.
For  your  calculations  you  will  need  to  solve  a transcendent equation, you can do it numerically or graphically.  With the b-value determined, find the wavelength the Sun and human body most efficiently emit.  

![Graph ][graph]

## Code Comments

This week we explore the different ways of solving polynomials.

For low degree polynomials one can use the quadratic equation, however
for 5 degree or higher there are no general analytical solutions.

The general structure of approximating roots goes like this:

1. Start with Initial Guess
2. Calculate the result of the guess
3. Update the guess based on the result
4. Repeat until satisfied

### Bisection Method

Start with two guesses such that f(guess_1) and f(guess_2) are of opposite sign. This means that we have one guess that’s too large and another guess that’s too small, then gradually squeeze the guess that’s too high and the guess that’s too low towards zero until the range between the two is small enough or equal to zero.

At each step take the midpoint of the two guesses. If the midpoint is zero (the guesses are the same) or if the guesses are sufficiently close to one another, return the midpoint. Otherwise, if the f(midpoint) is negative, then replace the lower bound with the midpoint, and if f(midpoint) is positive, then replace the upper bound with the midpoint.

### Newton Raphson Method

![Newton-Raphson-Method][Newtons]

The derivative tells us about the direction and step size to take on reasonably convex, continuous, well-behaved functions; all that is needed is find a point on the curve where the derivative is zero

For Newton-Raphson, we supply an initial guess, calculate the derivative of f at the initial guess, calculate where the derivative intersects the x-axis, and use that as our next guess.  The method can be extended to n dimensions with the Jacobian and/or higher orders of the Taylor series expansion, but for now we’ll keep it simple.

### Quasi-Newtonian: Secant Method

![Secent Method][secent]

The idea of the Quasi-Newtonian Secant Method and other Quasi-Newtonian methods is to substitute the expensive calculation of the derivative/Jacobian/Hessian at each step with an inexpensive but good-enough approximation.

Secent-Method is "derivative-like": approximate the derivative using two points (x0, f(x0)) and (x1, f(x1)), calculate where the line intercepts the x-axis, and use that as one of our new points, generating a line that should approximate the tangent line to the function somewhere between these two points

### Lagrange Polynomials

![Lagrange Polynomials Method][lagrange]

Initialized with three points, interpolates a polynomial curve based on those points, calculates where the curve intercepts the x-axis and uses this point as the new guess in the next iteration.

![Lagrange Polynomials Method][lagrangepic]


## Why does it matter?

The rate of convergence is of great importance in computing, as well as
the computational expense in each step of the iteration.

### Discussion

#### Bisection
The most robust and easy to use: go to for finding an approximation,
however it is incredibly slow!

#### Newton-Raphson
Converges fast but a good initial guess is needed. Since it is using the derivative, the computational cost is high.

#### Secent
Converges also linearly but faster than Newtons since it is not as computationally expensive, however it is also requiring a good initial guess.

#### Lagrange
Normally not used as a root finding algorithm



[Newtons]: https://github.com/fusionby2030/Uni_Work_SS20/tree/master/EP4/HW_03/files/newton_raphson.png "newton_raphson"

[lagrange]: https://github.com/fusionby2030/Uni_Work_SS20/tree/master/EP4/HW_03/files/lagrangepolynomial.png "lagrange"

[secent]: https://github.com/fusionby2030/Uni_Work_SS20/tree/master/EP4/HW_03/files/secentmethod.png "Secent"

[lagrangepic]: https://github.com/fusionby2030/Uni_Work_SS20/tree/master/EP4/HW_03/files/lagrangepic.png "lagrange"

[graph]: https://github.com/fusionby2030/Uni_Work_SS20/tree/master/EP4/HW_03/files/Figure_1.png "Figure_1"
