import pandas as pd
import numpy as np

str = pd.Series(['Mauricio', 'FATEC', np.nan, 'Professor'])
str

#Series sao como vetores porem pode alterar o index do valor. colocar a posicao 0 como sendo posicao 'd'

str[0] = None
str.isnull()