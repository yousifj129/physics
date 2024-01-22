from scipy import special as sp
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import cm

a = 0.5291 * (10 ** -10)
l = 0
m = 0
n = 1
r = np.linspace(0, 100, 100)
theta = np.linspace(0, math.pi, 10)
phi = np.linspace(0, 2 * math.pi, 10)

Psi = np.zeros((len(r), len(theta), len(phi)))

for i in range(len(r)):
    for j in range(len(theta)):
        for k in range(len(phi)):
            L_nk = sp.assoc_laguerre((2 * r[i]) / a, n - l - 1, (2 * l) + 1)
            Y_lm = sp.sph_harm(m, l, phi[k], theta[j])
            Psi[i, j, k] = (
                math.sqrt(((2 / a) ** 3) * ((math.factorial(n - l - 1)) / (2 * n * (math.factorial(n + l))))) *
                (math.e ** (-r[i] / a)) *
                ((2 * r[i] / a) ** l) *
                L_nk *
                Y_lm
            )

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

R, Theta, Phi = np.meshgrid(r, theta, phi)

X = (R * np.sin(Theta) * np.cos(Phi)).reshape(-2)
Y = (R * np.sin(Theta) * np.sin(Phi)).reshape(-2)
Z = (R * np.cos(Theta)).reshape(-2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

vmin = np.min(R)
vmax = np.max(R)
mid = max(abs(vmin), abs(vmax))
norm = plt.Normalize(-mid, mid)
cmap = plt.cm.get_cmap('viridis')

ax.plot_trisurf(X, Y, Z, cmap=cmap, norm=norm, linewidth=0.2)

plt.title('3D plot of Psi(r, theta, phi)')
plt.show()