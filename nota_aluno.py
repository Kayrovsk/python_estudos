# Solicitar nome do aluno
nome = input("Qual o seu nome? ")

# Ler notas dos alunos
while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("digite a terceira nota: "))
        
        if (
            nota1 < 0 or nota1 > 10 or
            nota2 < 0 or nota2 > 10 or
            nota3 < 0 or nota3 > 10
        ):
            print("As notas devem estar entre 0 e 10.")
            continue # Volta pro while

        break # Só chega aqui se tudo for ínvalido
    
    except ValueError:
        print("Erro! Digite apenas números.")

# Calcular a média dos alunos
media = (nota1 + nota2 + nota3) / 3

# Verificar se o aluno esta aprovado ou reprovado
if media >= 7:
    print(f"Olá, {nome}! Sua média é {media:.2f}.")
    print("Aluno aprovado!")

elif media >= 5 and media < 7:
    print(f"Olá, {nome}! Sua média é {media:.2f}.")
    print("Aluno em recuperação.")

else:
    print(f"Olá, {nome}! Sua média é {media:.2f}.")
    print("Aluno reprovado.")
