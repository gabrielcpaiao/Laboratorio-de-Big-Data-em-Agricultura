import pandas as pd
import numpy as np

numeros = pd.DataFrame(np.random.randn (10, 4))

print(numeros)

print()

print(numeros.describe())

col = numeros[2]

print()

print(col [np.abs(col) > 3])

print()

print(numeros[(np.abs(numeros) > 3).any(axis=1)])

numeros[np.abs(numeros)>3] = np.sign(numeros) * 3
numeros.describe()