"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    num = int(input('Digite um numero inteiro: '))
    if num %2==0:
        print('O numero Digitado é par!')
    else:
        print('o numero Digitado é impar!')
except ValueError:
    print('O valor digitado nao é um numero inteiro!')


print ('-'*40)
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
nome = input('como é seu nome?')
hora = int(input('Que horas são na sua cidade? '))
if hora <= 11:
    print(f'Bom Dia {nome}!')
elif hora >= 12 and hora <=17:
    print(f'Boa Tarde {nome}!')
else:
    print (f'Boa Noite {nome}!')


print ('-'*40)
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = str(input('Digite seu Primeiro Nome: '))
tamanho = len(nome)
if tamanho <= 4:
    print('Seu Nome é curto')
elif tamanho >=5 and tamanho <= 6:
    print('Seu Nome é normal')
else:
    print ('Seu Nome é grande')
