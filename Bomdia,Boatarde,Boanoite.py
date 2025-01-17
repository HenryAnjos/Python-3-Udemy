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