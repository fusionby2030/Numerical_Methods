import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
domain = np.linspace(0, 10, num=500)
A_x = 0.5
A_y = 0.5
omega_x = 1
omega_y = 1
phi_x = 0
phi_y = 0
x_domain = np.linspace(-2, 2, num=50)
y_domain = np.linspace(-2, 2, num=50)
X, Y = np.meshgrid(x_domain, y_domain)
hplicht = A_x*np.cos(2*np.pi*omega_x*0 + phi_x)
vplicht = A_y*np.cos(2*np.pi*omega_y*domain + phi_y)
u = np.cos(X)
v = np.cos(Y)
fig, ax = plt.subplots(figsize=(15,15))

zero_axis = np.zeros_like(X)
ax.quiver(0, 0, 10, 0, color=pink)
ax.quiver(0, 0, 0, 10, color=green)
ax.quiver(0, 0, 10, 10, color=gold)
#ax.quiver(x_domain, y_domain, 0, vplicht)
ax.set_aspect('equal')
t = 0
plt.quiver(X, Y, hplicht, 0, color=pink)
