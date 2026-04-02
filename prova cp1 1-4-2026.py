nome = input("digite o nome do cliente: ")
valor = float(input("Digite o valor da compra: "))
tipo = input("Digite o tipo de cliente (comum/premium)").lower()

if tipo == "comum":
    if _____:
        desconto = valor * 0.10
    else:
        desconto = valor * 0.05
elif ______:
    if valor >= 200:
        desconto = valor * 0.20
    else:
        desconto = valor * 0.10
else:
    desconto = 0
    print("______") # mensagem erro
    
    
if _____:
    valor_final = valor - desconto
    print("Cliente:", nome)
    print("Valor da compra:", valor)
    print("Desconto:", desconto)
    print("Valor final:", valor_final)
    
#complete oq ta faltando q está com ____

nome = input("Digite o nome do cliente: ")
valor = float(input("Digite o valor da compra: "))
tipo = input("Digite o tipo de cliente (comum/premium): ").lower()

if tipo == "comum":
    if valor >= 100:
        desconto = valor * 0.10
    else:
        desconto = valor * 0.05
elif tipo == "premium":
    if valor >= 200:
        desconto = valor * 0.20
    else:
        desconto = valor * 0.10
else:
    desconto = 0
    print("Tipo de cliente inválido, use comum ou premium.") #mensagem de erro

if tipo in ("comum", "premium"):
    valor_final = valor - desconto
    print("Cliente:", nome)
    print("Valor da compra:", valor)
    print("Desconto:", desconto)
    print("Valor final:", valor_final)
    
    
    
    



a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("\nOperações disponiveis:")
print("1: Adição")
print("2: Subtração")
print("3: Multiplicação")
print("4: Divisão")


operacao = input("Selecione a operação (1 a 4): ").strip()

if operacao == "1":
    resultado = a + b
    print("Resultado é:", resultado)
    
elif operacao == "2":
    resultado = a - b
    print("Resultado é:", resultado)
    
elif operacao == "3":
    resultado = a * b
    print("Resultado é:", resultado)
    
elif operacao == "4":
    if b == 0:
        print("erro! não é possível dividir por zero.")
    else:
        resultado = a / b
        print("Resultado é:", resultado)
else:
    print("erro! operação invalida, escolha um número de 1 a 4.")

    
