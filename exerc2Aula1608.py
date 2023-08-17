import pandas as pd
import numpy as np

idades = pd.Series([10, 5, 8, -99, 24, -99, 25, -99, 7, 12, -99])
newIdades = idades.replace(-99, 'NaN')

print(newIdades)