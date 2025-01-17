#faça um programa usando operador de comparação com numero
primeiro_valor = int(input('Digite um numero: '))
segundo_valor = int(input('Digite um numero: '))

if primeiro_valor < segundo_valor:
    print (f'o primeiro numero({primeiro_valor}) é menor que o segundo numero ({segundo_valor})')
elif primeiro_valor > segundo_valor:
    print (f' o primeiro numero ({primeiro_valor}) é maior que o segundo numero({segundo_valor})')
else:
    print (f' o primeiro numero ({primeiro_valor}) é igual ao segundo numero({segundo_valor})')