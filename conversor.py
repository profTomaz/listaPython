def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("Conversor Dólar x Real")
preco = float(input("Digite o Preço do produto em Dólar"))
resultado = converter(preco)
print(f"O valor em Reais é:{resultado:.2f}")