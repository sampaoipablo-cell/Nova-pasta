# Entrada do valor da compra
valor_compra = float(input("Digite o valor da compra (R$): "))

# Define a porcentagem do desconto
if valor_compra < 200:
    desconto = 0.05
elif valor_compra < 300:
    desconto = 0.10
else:
    desconto = 0.15

# Calculo dos valores
valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

# Exibição dos resultados
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {valor_final:.2f}")