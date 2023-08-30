import pandas as pd
from sklearn.preprocessing import LabelEncoder #transforma variavel categorica em numerica
from sklearn.naive_bayes import GaussianNB

base = pd.read_csv("risco_credito.csv", sep=";")
base

x_risco = base.iloc[ : ,0:4].values
x_risco

y_risco = base.iloc[ : ,4].values
y_risco

label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantia = LabelEncoder()
label_encoder_renda = LabelEncoder()

x_risco[:,0] = label_encoder_historia.fit_transform(x_risco[:,0])

x_risco[:,1] = label_encoder_divida.fit_transform(x_risco[:,0])

x_risco[:,2] = label_encoder_garantia.fit_transform(x_risco[:,2])

x_risco[:,3] = label_encoder_renda.fit_transform(x_risco[:,3])

x_risco


#Aplicando o Naive Bayes
#treinamento do algoritmo
naive_risco_credito = GaussianNB()
naive_risco_credito.fit(x_risco, y_risco)




#previsões
#historia = Boa 0, Divida = alta 0, garantia = nenhuma 1, renda >= 35 2
#historia = ruim 2, divida = alta 0, garantia = adequada 0, renda
previsao = naive_risco_credito.predict([[0,0,1,2], [2,0,0,0]])
previsao
