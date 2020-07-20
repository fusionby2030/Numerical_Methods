# HW_09

## Problems

1. Find average distance of the particle from the center of a potential field.

2. Inspect the hydrogen-like atom expected radius values.

3. Find average kinetic and potential energy of the electron in the ground state hydrogen atom.

4. Electron angular momentum and maximal projection for an electron in the d-state.

## Code Comments
This is a script, not intended to be used on its own or imported.
### problem1.py and problem2.py
Plotting the probability distribution and wave function with respect to distance. The wave function is first created by the lambda expression _wf_. In order to find the expected value, we use the scipy integrate module to check against the sum of the probability weighted domain.

Graphs below:
![<r> for a given psi][expec1]

![<r> vs <1/r> for a ground state hydrogen-atom n=1, l=0][expec2]

![<r> vs <1/r> for a ground state hydrogen-atom n=2, l=0][expec3]


[expec1]:files/problem1.png


[expec2]: files/problem2.png


[expec3]: files/problem21.png
