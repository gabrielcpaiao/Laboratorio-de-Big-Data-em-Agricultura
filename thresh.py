import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 3))
print(df)

df.iloc[:4, 1] = np.nan  # Usando np.nan para representar valores ausentes
df.iloc[:2, 2] = np.nan  # Usando np.nan para representar valores ausentes

print()

result_df = df.dropna(thresh=2)

print(result_df)

#todos os NA serao substituidos por 0
df.fillna(0)