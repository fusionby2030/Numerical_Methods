# HW_06

## Problems

1. Find the probability density of a linear combination (superposition) of two stationary wave functions.

2. Which energy is requirements for photons emitted from a particle which is localized in a region of a potential step.

![Potential Step][pstep]

3. Obtain the wave functions for the potential step described in 2. and derive the reflection and transition coefficients.  

## Code Comments

### potentialstep.py
This code animates a particle arriving at a potential step/barrier by creating a _Wave Packet_ class that has the following parameters:

- psi: array of current real and imaginary values for the given x and t domains of the wave function
- potential: array representing where the potential step is occurring
- evolution_matrix: array composed of the numerically calculated hamiltonian matrix that is used to evolve psi over time.

and the following functions:
- init: initializes all the parameters
- evolve: dots the evolution matrix with the current psi and returns the current probability

We also utilize matplotlib and have an _Animator_ class that takes the evolved values and graphs them over time.

To run, one must clone the repository, have the necessary packages (scipy, numpy, matplotlib), and using the terminal: `python potentialstep.py`

### superposition.py
Here we simply create wave functions for two different waves as well as their linear superposition, and graph their probability densities as functions of radius.

The result is below.

![Wave function and Probability densities of a superposition as functions of radius][superpos]


[pstep]: https://github.com/fusionby2030/Numerical_Methods/edit/master/EP4/HW_06/files/potentialstepdrawing.png "Potential Step Drawing"
[superpos]: https://github.com/fusionby2030/Numerical_Methods/edit/master/EP4/HW_06/files/superposition1.png "Superposition"
