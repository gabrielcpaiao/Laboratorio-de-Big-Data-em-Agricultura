'''
A base de dados
https://archive.ics.uci.edu/ml/datasets/Computer+Hardware

Apresenta o desempenho de computadores medido através de vários parâmetros. 
Aplique em primeiro momento a regressão linear simples, usando como valores 
de X e Y , respectivamente MMAX (memória principal máxima e ERP - desempenho 
estimado do computador).  Após isso, refaça para uma regressão múltipla, 
inserindo demais valores a X que também contribuem para o desempenho... Compares as devidas precisões.



Summary Statistics:
    Min     Max  Mean  SD      PRP     Correlation
    MCYT:   17   1500  203.8   260.3   -0.3071
    MMIN:   64   32000 2868.0  3878.7   0.7949
    MMAX:   64   64000 11796.1 11726.6  0.8630
    CACH:   0    256   25.2    40.6     0.6626
    CHMIN:  0    52    4.7     6.8      0.6089
    CHMAX:  0    176   18.2    26.0     0.6052
    PRP:    6    1150  105.6   160.8    1.0000
    ERP:   15    1238  99.3    154.8    0.9665
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm


base = pd.read_csv("/content/machine.data")
base


plt.figure(figsize=(16,8))
plt.scatter(
    base['MMAX'],
    base['ERP'],
    c='red')

plt.xlabel(" MMAX ")
plt.ylabel(" ERP ")
plt.show()


x = base['MMAX'].values.reshape(-1,1)
y = base['ERP'].values.reshape(-1,1)


reg = LinearRegression()
reg.fit(x, y)
print("O modelo é: DESEMPENHO EM RELAÇÃO MMAX e ERP = {:.5} + {:.5}x".format(reg.intercept_[0], reg.coef_[0][0]))


f_previsoes = reg.predict(x)

plt.figure(figsize=(16,8))
plt.scatter(
    base['MMAX'],
    base['ERP'],
    c='red'
)



plt.plot(
    base['MMAX'],
    f_previsoes,
    c='blue',
    linewidth=3,
    linestyle=':'
)


plt.xlabel(" MMAX ")
plt.ylabel(" ERP ")
plt.show()


x = base['MMAX']
y = base['ERP']
x2 = sm.add_constant(x)
est = sm.OLS(y, x2) #dados de estatístca
est2 = est.fit() #dados de estatístca
print(est2.summary())



from sklearn.linear_model import LinearRegression
xs = base.drop(['ERP', 'vendor name', 'Model name'], axis=1)
y = base['ERP'].values.reshape(-1,1)
rl = LinearRegression()
rl.fit(xs, y)


x = np.column_stack((base['MMAX'], base['CACH'], base['MYCT']))
y = base['ERP']

x2 = sm.add_constant(x)
est = sm.OLS(y, x2)
est2 = est.fit()

print(est2.summary())