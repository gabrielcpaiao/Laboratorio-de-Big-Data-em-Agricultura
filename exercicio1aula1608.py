#series com 10 e algumas delas com NA
#use filna substituir dados ausentes pela media das notas
#paraa media use notas validas

import pandas as pd
import numpy as np

# Cria uma Series com 10 valores, incluindo alguns valores NaN
data = pd.Series([8, 7, np.nan, 9, 6, np.nan, 7, np.nan, 8, 9])

# Calcula a média dos valores não nulos
media = data.dropna().mean()

# Preenche os valores NaN com a média calculada
data_filled = data.fillna(media)

print("Series original:")
print(data)
print("\nMédia:", media)
print("\nSeries após preenchimento:")
print(data_filled)
