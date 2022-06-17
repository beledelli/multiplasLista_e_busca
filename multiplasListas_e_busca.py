nome=[]
idade=[]
cidade=[]
continuar="S"

while continuar=="S":
    nome.append(input("Nome: "))
    try:
        idade.append(int(input("Idade: ")))
    except:
        idade.append(int(input("Digite somente numeros na idade.\nIdade: ")))
    cidade.append(input("Cidade: "))
    continuar=input("Deseja continuar? S/N\n").upper()

busca=input("Qual o nome que deseja buscar: ")
for indice in range (0, len(nome)):
    if busca==nome[indice]:
        print(f"\nNome: {nome[indice]}\nIdade: {idade[indice]}\nCidade: {cidade[indice]}")
        break
    else:
        print("Nome não cadastrado")
        break

