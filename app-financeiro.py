# Aplicativo de depósito, saque e saldo
name = input("Digite seu nome: ")
app = "on"

print(f'Bem vindo {name}!')

balance = 0.0
limit = 500.00
w_limit = 3
w_made = 0
bank_statement = []


while (app == "on"):
    print ("-------------------------------------------")
    print('Digite o número da opção que você deseja:')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Ver extrato')
    print('0 - Sair')
    print(' ')
    try:
        option = int(input("Digite aqui: "))
    except:
        print('Digite apenas o número da opção!')
        continue
    print(' ')
    if option == 1:
        print (f'Seu saldo é de R${balance:.2f}')
        print ("-------------------------------------------")
        input('Tecle enter para continuar...')
        print(' ')
        print(' ')
    elif option == 2:
        depositing = True
        while depositing:
            try:
                deposit = float(input("Digite o valor do depósito: "))
                print(' ')
            except:
                print(' ')
                print('Depósito não realizado:')
                print('Verifique o valor digitado, deve ser no formato 0000.00, e não pode ser negativo!')
                print("-------------------------------------------")
                input('Tecle enter para continuar...')
                print(' ')
                continue

            if deposit < 0:
                print('Depósito não realizado: Valor de depósito não pode ser negativo!')
                input('Tecle enter para continuar...')
                print(' ')
                continue
                
            print (f'Seu depósito é de R${deposit:.2f}?')
            confirm = input("[Y] Yes | [N] No :  ")
            print(' ')
            if confirm in ("Y","y","Yes","yes","YES"):
                balance += deposit
                bank_statement.append(f"Depósito: + R${str(deposit)}")
                print(f'Depósito de R${deposit:.2f} realizado com sucesso!')
                depositing = False
            else:
                print('Depósito não realizado: Falha na confirmação, use Y para confirmar')
                print(' ')
                continue
        print ("-------------------------------------------")
        input('Tecle enter para continuar...')
        print(' ')
        print(' ')
    elif option == 3:
        if w_limit - w_made == 0:
            print('Você atingiu o seu limite de saques!')
            print("-------------------------------------------")
            input('Tecle enter para continuar...')
            print(' ')
            continue
        withdrawing = True
        while withdrawing:
            try:
                withdraw = float(input("Digite o valor do saque: "))
                print(' ')
            except:
                print(' ')
                print('Saque não realizado:')
                print('Verifique o valor digitado, deve ser no formato 0000.00, e não pode ser negativo!')
                print("-------------------------------------------")
                input('Tecle enter para continuar...')
                print(' ')
                continue

            if withdraw < 0:
                print('Saque não realizado: Valor de saque não pode ser negativo!')
                input('Tecle enter para continuar...')
                print(' ')
                continue

            if withdraw > balance:
                print('Saque não realizado: Saldo insuficiente para saque!')
                print (f'Seu saldo atual é de R${balance:.2f}')
                input('Tecle enter para continuar...')
                print(' ')
                continue

            if withdraw > limit:
                print('Saque não realizado: Limite de R$500.00 por saque!')
                input('Tecle enter para continuar...')
                print(' ')
                continue
                
            print (f'Você quer sacar R${withdraw:.2f}?')
            confirm = input("[Y] Yes | [N] No :  ")
            print(' ')
            if confirm in ("Y","y","Yes","yes","YES"):
                balance -= withdraw
                bank_statement.append(f"Saque: - R${str(withdraw)}")
                print(f'Saque de R${withdraw:.2f} realizado com sucesso!')
                w_made += 1
                withdrawing = False
            else:
                print('Saque não realizado: Falha na confirmação, use Y para confirmar.')
                print(' ')
                continue
        print ("-------------------------------------------")
        input('Tecle enter para continuar...')
        print(' ')
        print(' ')
    elif option == 4:
        print("================ EXTRATO ================")
        if len(bank_statement) > 0:
            for transaction in bank_statement:
                print(transaction)
        else:
            print("Nenhuma transação efetuada")
        print (f'Seu saldo atual é de R${balance:.2f}')
        print ("-------------------------------------------")
        input('Tecle enter para continuar...')
        print(' ')
        print(' ')
    elif option == 0:
        app = "off"
    else:
        print ("Opção inválida")
        print ("-------------------------------------------")
        input('Tecle enter para continuar...')
        print(' ')
        print(' ')
        continue

print("Aplicativo encerrado.")