menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informeo valor dp depósito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou. Valor Inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))
        valor_excedeu = valor > saldo
        limite_excedeu = valor > limite
        saques_excedeu = numero_saques >= LIMITE_SAQUES

        if valor_excedeu:
            print("Operação falhou. Você não tem saldo suficiente")
        elif limite_excedeu:
            print("Operação falhou. Valor excede o limite disponível")
        elif saques_excedeu:
            print("Opereção falhou. Você atingiu o limite de saques disponíveis")
        elif valor>0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques +=1
        else:
            print("Operação falhou.Valor informado inválido")
        
    elif opcao == "e":
        print("\n====================EXTRATO===================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================================")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")