# SISTEMA CAIXA ELETRONICO
# Dados do úsuario
nome_usuario = "Kayro"
senha_user = "12A34B"
saldo = 1000.00

# Inicia o looping
while True:
    while True:
        # Solicita a senha do usuario
        senha_digitada = input("Digite sua senha de 6 digitos para continuar: ")
        if senha_user != senha_digitada:
            print("Senha incorreta! Tente novamente.")
            continue # Volta ao inicio do loop
        else:
            print("Acesso confirmado!")
            break
    
    while True:
        # MENU DO SISTEMA
        escolher_opcoes = input("1 Saldo \n2 Deposito \n3 Saque \n4 Sair: \n")

        # Ver saldo do usuario
        if escolher_opcoes != "1" and escolher_opcoes != "2" and escolher_opcoes != "3" and escolher_opcoes != "4":
            print("Escolha uma opção valida.")
            continue

        elif escolher_opcoes == "1":
            print(f"Seu saldo disponivel é {saldo:.2f}")

        # Depositar saldo
        elif escolher_opcoes == "2":
            try:
                deposito = float(input("Qual o valor do deposito?: "))
                if deposito <= 0:
                    print("O valor deve ser maior que zero.")
                    continue
                saldo += deposito
                print(f"Saldo atual é de {saldo:.2f}")

            except ValueError as e:
                print("Deposito invalido.")
                continue

        # Sacar
        elif escolher_opcoes == "3":
            try:
                saque = float(input("Qual valor deseja sacar? "))
                if saque < 0:
                    print("Saque deve ser maior que zero.")
                    continue
                if saque > saldo:
                    print("Saldo insuficiente.")
                    continue

                saldo -= saque
                print(f"Saldo atual {saldo:.2f}")
            
            except ValueError as e:
                print("Valor invalido.")
                continue
                 
        # Sair
        elif escolher_opcoes == "4":
            print("Seção encerrada. Até mais!")
                
        break
            

