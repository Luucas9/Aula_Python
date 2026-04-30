#ex 1 criand um dataframe
#dia 29/04/2026

import pandas as pd

dados = {
    
    'nome': ['ana', 'bruno', 'carlos', 'lucas', 'pedro'],
    'idade': [23, 35, 29, 40, 18],
    'salario': [2000, 5000, 3000, 7000, 10000]
    
    }


df = pd.Dataframe(dados)

for i in range(len(df)):
    if df.loc[i, 'idade'] > 30:
        print(df.loc[i, 'nome'])
        
#ex 3

for i in range(len(df)):
    salario = df.loc[i, 'salario']
    
    if salario < 3000:
        print("Baixo")
    elif salario < 6000:
        print("Médio")
    else:
        print("Alto")
        
#ex 4 - acumular valores

soma = 0

for valor in df['salario']:
    soma += i
    
    print(soma)
    
#ex 5 - exemplo com hwile

i = 0

while i < len(df):
    print(df.loc[i, 'nome'])
    
    i += 1