menu = """

---- MENU ----

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito efetuado!")
  
        else:
            print("\nInforme um valor válido!")
    
    elif opção == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nSaldo insuficiente para saque!")

        elif excedeu_limite:
            print("\nLimite diário insuficiente. Contate seu gerente!")

        elif excedeu_saques:
            print("\nNúmero de saques excedidos. Volte amanhã!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado! Obrigado!")

        else:
            print("\nOperação falhou! Digite um valor válido.")   
    
    elif opção == "3":
        print("\n######## EXTRATO ########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###########################")
    
    
    elif opção == "4":
        break
    
    else:
        print("\nOperação não reconhecida, digite uma opção válida!")