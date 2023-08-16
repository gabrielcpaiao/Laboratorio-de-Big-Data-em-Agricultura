#dropna() filtra dados ausentes
import pandas as pd
import numpy as np

from numpy import nan as NA
notas = pd.Series([7.5, NA, 3.5, NA,  9.3])
print(notas.dropna())