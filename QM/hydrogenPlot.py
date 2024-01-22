from scipy import special as sp
import matplotlib.pyplot as plt
import numpy as np
import math

a = 0.5291 * (10 ** -10)
l = 1
m = 1
n = 2
r = np.linspace(0, 4, 4)
phi = np.linspace(0, 2 * math.pi, 100)

Psi = np.zeros((len(r), len(phi)))

for i in range(len(r)):
    for j in range(len(phi)):
        L_nk = sp.assoc_laguerre((2 * r[i]) / a, n - l - 1, (2 * l) + 1)
        Y_lm = sp.sph_harm(m, l, 0, phi[j])
        Psi[i, j] = (
            math.sqrt(((2 / a) ** 3) * ((math.factorial(n - l - 1)) / (2 * n * (math.factorial(n + l))))) *
            (math.e ** (-r[i] / a)) *
            ((2 * r[i] / a) ** l) *
            L_nk *
            Y_lm
        )


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='polar')
R, Phi = np.meshgrid(r, phi)

ax.contourf(Phi, R, np.abs(Psi.T), cmap='viridis')

ax.set_yticklabels([])
ax.set_xticklabels([])
ax.spines['polar'].set_visible(True)
ax.grid(True)

plt.title('Polar plot of Psi(r, phi)')
plt.show()