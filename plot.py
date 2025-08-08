import numpy as np
import matplotlib.pyplot as plt

# Les points d'exemple
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 2, 5, 7])

# On crée des valeurs x plus denses pour tracer les courbes lisses
x_dense = np.linspace(x.min(), x.max(), 100)

# Fonction pour tracer un polynôme d'un certain degré
def plot_polyfit(degree):
    coeffs = np.polyfit(x, y, degree)      # Calcul des coefficients du polynôme
    poly = np.poly1d(coeffs)                # Création de la fonction polynomiale
    y_dense = poly(x_dense)                 # Calcul des y correspondants aux x denses
    plt.plot(x_dense, y_dense, label=f"Degré {degree}")

plt.scatter(x, y, color='red', label='Points d\'origine')

# On trace les polynômes de degrés 1, 2, 4
for deg in [1, 2, 3, 6]:
    plot_polyfit(deg)

plt.legend()
plt.title("Ajustement polynômial selon le degré")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
