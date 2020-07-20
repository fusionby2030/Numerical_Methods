import numpy as np


input_x = np.array([3.5, 8.4, 16.8, 23.9, 27.1, 28.8])
output_y = np.array([4.4, 9.2, 20.6, 31.1, 35.0, 37.7])
np.sum(input_x*input_x*input_x*input_x)
function = lambda x: 0.1849 + 1.0762*x + 0.0081*x*x
domain = np.linspace(3, 35)
y = function(domain)
import matplotlib.pyplot as plt
plt.scatter(input_x, output_y, c='orange',label='Data Points')
plt.plot(domain, function(domain), label="Fit")
plt.legend()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/nmproblem1.png')
