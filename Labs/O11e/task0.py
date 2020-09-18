import numpy as np
import matplotlib.pyplot as plt

from py_pol import degrees
from py_pol.jones_vector import Jones_vector
from py_pol.jones_matrix import Jones_matrix, create_Jones_matrices

"""
Part a)
Linear Polarizer 
"""

# Incident wave
E0 = Jones_vector('Incident wave: Linear. Light')
E0.linear_light(intensity=1, azimuth=90 * degrees)
print(E0)

# analyser
P1 = Jones_matrix('Analyzer')
angles = np.linspace(0, 360 * degrees, 361)  # Steps of 1 degree
P1.diattenuator_perfect(azimuth=angles)

E_final = P1 * E0
E_final.name = 'Output wave'

I_perfect = E_final.parameters.intensity()

"""
b) Circulalry polarized light
"""

# Incident wave
E0 = Jones_vector('Incident wave: Circ. Light')
E0.circular_light(intensity=1)
print(E0)

# analyser
P1 = Jones_matrix('Analyser')
angles = np.linspace(0, 360 * degrees, 361)  # Steps of 1 degree
P1.diattenuator_perfect(azimuth=angles)

E_final = P1 * E0
E_final.name = 'Output wave'

I_perfect = E_final.parameters.intensity()

"""
Part c and D)
polarized light passing first through a lambda / 4 plate before entering linear analyser
"""


def wave_plate_sim(az, initial_setting='linpol'):
    # Incident Wave
    E0 = Jones_vector("Incident Wave:")
    if initial_setting == 'linpol':
        E0.linear_light(intensity=1)

    else:
        E0.circular_light(intensity=1)
    print(E0)
    # QW Plate
    M1 = create_Jones_matrices('Quarter Wave Plate')
    M1.quarter_waveplate(az * degrees)
    # Analyser
    P1 = Jones_matrix('Analyser')
    angles = np.linspace(0, 360 * degrees, 361)  # Steps of 1 degree
    P1.diattenuator_perfect(azimuth=angles)

    E_final = P1 * M1 * E0
    I_perfect = E_final.parameters.intensity()
    return I_perfect


# print(I_perfect)
angles1 = np.arange(0, 361)

for az in [0, 15, 30, 45, 60, 75, 90]:
    plt.plot(angles1, wave_plate_sim(az, initial_setting='linpol'), label='ang = {}'.format(az))
plt.ylabel('Intensity')
plt.xlabel('Analyser Angle')
plt.title('Circ. Light -> Quarter Wave Plate')
plt.legend()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/O11e/data/sim_d.png')
plt.show()
