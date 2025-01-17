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
