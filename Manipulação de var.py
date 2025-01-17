#seu nome é X
#Seu nome invertido é  X
#seu nome contem ou nao espaço X
#ultima e primeira letra do nome X




nome = input('Digite seu nome: ').strip()
idade = input('Digite sua idade: ').strip()
if nome and idade:
    print(f'Seu nome é {nome}')
    
    print(f'Seu nome invertido é {nome[::-1]}')

    if " " in nome:
        print('seu nome tem espaço')
    else:
        print('seu nome nao tem espaço')
        
    print(f'Seu nome tem {len(nome.replace(' ',''))} Letras')
    
    print(f'A ultima letra do seu nome é {nome[0]} e a ultima letra é {nome[-1]}')
else: 
    print('desculpe, Voce deixou campos vazios')