"""
Criar um sistema bancário em Python que utilize funções, resgistre histórico de operações e
mantenha validações de erro.
"""
# Dados do úsuario
nome = "Kayro"
senha = "12A34B"
saldo_conta = 0
extrato = []

# FUNÇÕES
def menu():
    print("1 - Deposito")
    print("2 - Saque")
    print("3 - Saldo")
    print("4 - Extrato")
    print("5 - Sair")

def depositar(saldo, valor):
    return saldo + valor

def sacar(saldo, valor):
    if valor <= saldo:
        return saldo - valor
    else:
        print("Saldo insuficiente.")
        return saldo

def verSaldo(saldo):
    print(f"Saldo atual: R${saldo:.2f}")

# Iniciar programa
while True:
    while True:
        # Validação de senha
        solicita_senha = input("Digite sua senha para continuar: ")
        if solicita_senha != senha:
            print("Senha incorreta! Tente novamente.")
            continue    # Volta ao inicio

        else:
            print("Acesso confirmado!")
            break

    # Sistema de menu
    while True:
        menu()
        opcao = input("Escolha o que deseja: ")

        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
            print("Opção ínvalida! Tente novamente.")
            continue
        
        # Sistema de deposito
        elif opcao == "1":
            try:
                valor = float(input("Qual o valor deposistado? "))
                if valor > 0:
                    saldo_conta = depositar(saldo_conta, valor)
                    print(f"Deposito de R${valor:.2f} realizado!")
                    extrato.append(f"Deposito +{valor}")
                
                else:
                    print("Valor deve ser positivo!")
            except ValueError:
                print("Valor ínvalido!")

        # Sistema de saque
        elif opcao == "2":
            try:
                valor = float(input("Qual o valor do saque? "))
                if valor <= saldo_conta:
                    saldo_conta = sacar(saldo_conta, valor)
                    print(f"Saque de R${valor:.2f} efetuado com sucesso!")
                    extrato.append(f"Retirada -{valor}")
                    
                else:
                    print("Valor deve ser positivo!")
            except ValueError:
                print("Valor ínvalido!")

        # Sistema de saldo
        elif opcao == "3":
            verSaldo(saldo_conta)

        # Sistema de extrato
        elif opcao == "4":
            print(extrato)
            
        else:
            print("ATÉ A PRÓXIMA SEÇÃO!")
            break
        break
    break
