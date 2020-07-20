# HW_07

## Problems

1. Which quantity is adiabatic invariant for quantum harmonic oscillator?

2. In a 3 dimensional potential well, find the wave functions for stationary states.

3. Find the degeneracy of the energy level with quantum number n.

## Code Comments

### radialdist.py
Here we plot the 3d probability distribution of the hydrogen-like atom.

With the help of the below functions we are able to create distribution graphs in 1,2, and 3 dimensions.
For the 2d angular probability, one chooses value of Z to create the plane on which to view the density(_plot_angular_surface_).   

- Psi functions:
  - radial_wave_function
  - hrwfp
    - radial probability distribution of radial_wave_function
  - angular_function
  - hydrogen_angular_prob
    - probability distribution of angular_function
- Plotting functions:
  - plot_angular_surface
  - plot_radial_component
  - plot_radial_surface
- helper functions:
  - cartesian2spherical

To run the code one needs numpy, scipy, matplotlib, as well as choose which plotting function you would like to use. These can be inserted in the main part of the file.

Sample outputs of 3d plots  below:

![Radial Probability Distribution for n=3, l=1, m=1][rprob311]
![Radial Probability Distribution for n=3, l=2, m=1][rprob321]

### sym-tutor.py
A brief look at how Sympy works.

[rprob311]: files/hangdist31-1.png "Radial Wave Plot n=3, l=m=1"
[rprob321]: files/hangdist32-1.png "Radial Wave Plot n=3, l=2, m=1"
