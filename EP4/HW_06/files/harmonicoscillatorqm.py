from matplotlib import pyplot as plt
import numpy as np

2*np.pi**2/(N-1)
hbar=1
m=1
omega=1
N = 2016
a = 20.0
x = np.linspace(-a/2.,a/2.,N)
h = x[1]-x[0] # Should be equal to 2*np.pi/(N-1)
V = .5*m*omega*x*x
# V[N/2]=2/h   # This would add a "delta" spike in the center.
Mdd = 1./(h*h)*(np.diag(np.ones(N-1),-1) -2* np.diag(np.ones(N),0) + np.diag(np.ones(N-1),1))
H = -(hbar*hbar)/(2.0*m)*Mdd + np.diag(V)
En,psiT = np.linalg.eigh(H) # This computes the eigen values and eigenvectors
psi = np.transpose(psiT)

# The psi now contain the wave functions ordered so that
#psi[n] if the n-th eigen state.
# Check the normalization of the wave function arrays.
not_normalized = []
for n in range(len(psi)):
    # s = np.sum(psi[n]*psi[n])
    s = np.linalg.norm(psi[n])  # This does the same as the line above.
    if np.abs(s - 1) > 0.00001: # Check if it is different from one.
        print( "Wave function {} is not normalized to 1 but {}".format(n,s))
        not_normalized.append(n)

if not_normalized:
    for _ in not_normalized:
        print( " Psi_{} is not normailized.".format(n))
else:
    print( "All the psi_n(x) are normalized.")

fig2 = plt.figure(figsize=[10,7])
plt.title('Harmonic Oscillator')
plt.ylabel('$\psi(x)$')
plt.xlabel('$x$')
plt.plot([0,0],[-6,V[0]],color="blue")
plt.plot([-a/2.,a/2.],[0,0],color="blue")
plt.plot(x,0.1*V,color="grey",label="V(x) scaled by 0.1")
plt.ylim((-.8,1.))
plt.xlim((-6.,6.))
for i in range(0,5):
    if psi[i][int(N/8)] < 0:

        y = -psi[i]/np.sqrt(h)
        print(type(y))
        plt.plot(x,y,label="$E_{}$={:3.1f}".format(i,En[i]))
    else:
        y = psi[i]/np.sqrt(h)
        plt.plot(x,y,label="$E_{}$={:3.1f}".format(i,En[i]))

plt.title("Solution to harmonic oscillator")
plt.legend()
#plt.savefig("Harmonic_Oscillator_WaveFunctions.pdf")
plt.show()
