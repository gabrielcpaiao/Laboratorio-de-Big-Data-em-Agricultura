'''
Objetivo: Prever possível aprovação de crédito agrícola.
Características do conjunto de dados: Multivalorados;
Atributos: 5. Tipos: contínuo e inteiro;
Tarefa associada: Classificação;
Valores Faltantes: Sim.
'''

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler #padronizacao de dados
from sklearn.model_selection import train_test_split #quebrar a base em duas (uma p treinamento e outra pra teste)
from sklearn.naive_bayes import GaussianNB

base = pd.read_csv("credit-data.csv")
base

base.loc[base.age<0]

#Calcular media das idades validas
#med = base[base.age>0].mean()
med = base[base.age>0].mean().age
med


#colocar no lugar dos valores negativos a media calculada das colunas sem os valores negativos
base.loc[base.age<0,'age']= med

base


previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values


imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(previsores[:, 1:4])
previsores[:,1:4] = imputer.transform(previsores[:,1:4])



scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)


previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)



classificador = GaussianNB()
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)


