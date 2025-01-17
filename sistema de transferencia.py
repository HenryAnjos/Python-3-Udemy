try:
    saldo = float(input("Digite seu saldo: "))
    valor_transferencia = float(input("Digite o valor da transferência: "))

    if valor_transferencia > saldo:
        raise ValueError("Saldo insuficiente")
    else:
        print("Transferência realizada com sucesso!")
except ValueError:
    print(f"Erro: Digite um Numero!")