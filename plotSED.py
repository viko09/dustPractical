# Load libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
dataDat = pd.read_csv('galaxia_starbust_SED.txt',
                      sep='\s+', index_col=False)

# Set x and y axis
x = dataDat['lam(micras)']
y = dataDat['energia(erg/sec/micras)']

# Plot galaxy energy
plt.plot(x, y, label='Energía', color='orangered', alpha=0.65)
plt.xscale('log')
plt.yscale('log')
# Graphic settings
plt.title(r'SED de la Galaxia')
plt.xlabel('$\lambda$ (Micras)')
plt.ylabel('$Enegía$')
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()
plt.show()

# Maximum value
xVal = x.max()
yVal = y.max()
print(xVal, yVal)
xPosit = x.idxmax()
yPosit = y.idxmax()
print(xPosit, yPosit)

# Plot galaxy energy with MAX value
