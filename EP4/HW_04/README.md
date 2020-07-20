# HW_04

## Problems

1.  An electron performs under damped, but nearly harmonic, oscillations with a frequency of 10^15Hz.  After which time period it will loose 90% of its initial energyE0.

![Larmor formula for emitted power][leq]


2.  Find the average scattering angle ̄θ resulting for the Thomson model of atom.  Use the fact that the scattering angles are small.

3.  Find how the distance ∆r between two adjacent electron orbits varies with increasing radius in the limit of large quantum numbers n.  

4.  Show that the energy of the transitions between two adjacent orbits ∆E is proportional ton−3in the limit of large quantum numbers.  

5.  Which spectral lines will appear in the emission spectrum of an atomic hydrogen gas upon irradiating it with ultraviolet light with the wave length of 100 nm?  

### Initial Notes

We assume that for each problem where the number of electrons is not specified, that the number of electrons in each orbit is 1.

### Code Comments

#### electronorbit.py
For problem 3 and 4, we are able to represent the orbit distances and energies as a function of quantum numbers n and r.

![Orbital Radius for various quantum numbers][rtrans]  
![Transition Energy  for various quantum numbers][etrans]  


#### thomsonangle.py
Here I use Monte Carlo sampling so simulate the scattering of a particle as a random walk, and then take the mean angle scattered.

[leq]: files/larmoreq.png "Larmor Formula for emitted power"
[rtrans]: files/radiustrans.png "transitional orbital radius for various quantum numbers"
[etrans]: files/energytrans.png "transitional energy for various quantum numbers"
