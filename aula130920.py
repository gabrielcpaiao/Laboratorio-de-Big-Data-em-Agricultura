import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

base = pd.read_csv("Adversitiong.csv")
base

print(base.describe())

plt.figure(figsize=(16,8))
plt.scatter(
    base['TV'],
    base['sales'],
    c='red')

plt.xlabel(" ($) Gasto em propaganda de TV")
plt.ylabel(" ($) Vendas")
plt.show()

x = base['TV'].values.reshape(-1,1)
y = base['sales'].values.reshape(-1,1)

reg = LinearRegression()
reg.fit(x, y)
print("O modelo é: Vendas = {:.5} + {:.5}x".format(reg.intercept_[0], reg.coef_[0][0]))

#O modelo é: Vendas 7.0326 + 0.04753x

f_previsoes = reg.predict(x)

plt.figure(figsize=(16,8))
plt.scatter(
    base['TV'],
    base['sales'],
    c='red'
)

plt.plot(
    base['TV'],
    f_previsoes,
    c='blue',
    linewidth=3,
    linestyle=':'
)

plt.xlabel(" ($) Gasto em propaganda de TV")
plt.ylabel(" ($) Vendas")
plt.show()

x = base['TV']
y = base['sales']
x2 = sm.add_constant(x)
est = sm.OLS(y, x2) #dados de estatístca
est2 = est.fit() #dados de estatístca
print(est2.summary())



from sklearn.linear_model import LinearRegression
xs = base.drop(['sales', 'Unnamed: 0'], axis=1)
y = base['sales'].values.reshape(-1,1)
rl = LinearRegression()
rl.fit(xs, y)

print("O modelo é: Vendas = {:.5} + {:.5}*TV + {:.5}radio + {:.5}*newspaper".format(rl.intercept_[0], rl.coef_[0][0], rl.coef_[0][1], rl.coef_[0][2]))
#O modelo é: Vendas = 2.9389 + 0.045765*TV + 0.18853*radio + -0.0010375*newspaper


x = np.column_stack((base['TV'], base['radio'], base['newspaper']))
y = base['sales']

x2 = sm.add_constant(x)
est = sm.OLS(y, x2)
est2 = est.fit()

print(est2.summary())