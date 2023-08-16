#com DataFrame qualquer 'linha' que tiver pelo menos um NA será descartada
import pandas as pd
import numpy as np

dados = pd.DataFrame([['Ana', 7.5, 8.5], ['Luis', NA, NA], [NA, NA, NA], ['Maria', 6.5, NA]])


dados_limpos = dados.dropna()
dados_limpos


'''

import pandas as pd
import numpy as np

dados = pd.DataFrame([['Ana', 7.5, 8.5], ['Luis', NA, NA], [NA, NA, NA], ['Maria', 6.5, NA]])

# Replace NaN values in the 'nota2' column with the mean of the column
dados['nota2'].fillna(dados['nota2'].mean(), inplace=True)

print(dados)


'''