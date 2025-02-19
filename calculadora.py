while True:
    print ('-'*40)
    try:
        num1 = int(input('Digite um Numero: '))
        num2 = int(input('Digite mais um Numero: '))
    except ValueError:   
        print('ERRO: DIGITE APENAS NUMEROS!')
        break
    sair = input('Deseja sair?: ').lower().startswith('s')
    if sair is True:
        print ('Saindo...')
    else:
        print ('''
            Voçe deseja:
            (1)Multiplicar
            (2)Somar
            (3)Subtrair
            (4)Dividir
            (5)Sair
            ''')
        operador = int(input('Digite uma das opções: '))
        if operador == 1:
            multiplicação =num1 * num2
            print(multiplicação)
        elif operador == 2:
            soma = num1 + num2
            print (soma)
        elif operador == 3:
            subtrair = num1 - num2
            print (subtrair)
        elif operador == 4:
            dividir = num1/num2
            print(dividir)
        elif operador == 5:
            print ('Saindo...')
            break
        