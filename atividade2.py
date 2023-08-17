'''
Fatec Pompeia Shunji Nishimura
Laboratorio de Big Data em Agricultura
Professor: Maurício Duarte
Aluno: Gabriel Costa Paião

Criar Series 20 notas de alunos
Notas entre 0 e 10
As notas fora desse intervalo: menores que 0 para 0 e maiores que 10 para 10

https://acervolima.com/numpy-clip-em-python/
'''

import pandas as pd
import numpy as np

#notas = pd.Series(np.random.randint(-5, 16, size=20))
notas = pd.Series([8, 7, -3, 9, 6, 16, 7, -12, 8, 9, 8, 7, -3, 9, 6, 16, 7, -12, 8, 9])

print(notas)

print()

min_value = 0
max_value = 10

#notas[(np.abs(notas) > 10)].replace()
#notas = np.where(notas < 0, 0, np.where(notas > 10, 10, notas))
#clipped_notas = [min(max(value, min_value), max_value) for value in notas]
clipar = np.clip(notas, min_value, max_value)
print(clipar)