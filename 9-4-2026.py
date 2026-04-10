# 4 - separar valores inseridos  pelo usuario em duas listas (par e impar)

lista_completa = []
lista_par = []
lista_impar = []

for k in range(10):
    numeros = int(input(f"Digite o {k+1} numero "))
    
    lista_completa.append(numeros)
    
    if numeros %2 == 0:
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)
        
    
print(lista_par)
print(lista_impar)
print(lista_completa)

#==================

#ex 5: mostrar o preco final da compra e a média

lista_preco = []

soma = 0

for k in range(5):
    preco = int(input(f"Digite o preco {k+1} "))
    
    lista_preco.append(preco)
    # soma dos produtos
    soma += preco

#media das compras
media = soma / len(lista_preco)
print(soma)
print(media)

#ex6 - estruturas com break e continue

lista_nomes = ['ana', 'laura', 'paulo', 'jose', 'greice']

for k in lista_nomes:
    if k == 'paulo':
        continue
    
    print(k)
    
##################################################

lista_nomes = ['ana', 'laura', 'paulo', 'jose', 'greice']

for k in lista_nomes:
    
    if k == 'paulo':
        break
    
    print(k)
    
#Ex.1: Escreva um programa que identifique quais valores são pares em um range de 1 a 50 e calcule a média destes valores.


pares = []

# Percorrendo o range de 1 a 50
for num in range(1, 51):
    if num % 2 == 0:
        pares.append(num)
        
# Calculando a média
media = sum(pares) / len(pares)

# Exibindo os resultados
print("Números pares:", pares)
print("Média dos pares:", media)

##############

#Ex.2: Crie um programa que imprima quais são os números pares de 1 a 50 e calcule a soma 
#dos valores pares.

pares = []

# Percorrendo o range de 1 a 50
for num in range(1, 51):
    if num % 2 == 0:
        pares.append(num)
        
# soma

soma = sum(pares)

print("Pares:", pares)
print("Soma:", soma)

#Ex.3: Crie um algoritmo no qual o usuário insira valores,
#identifique quais números são pares, some e calcule a média dos valores
#pares escolhidos pelo usuário.

pares = []
numeros = []

