class Livro:
    def __init__(self, name, date, author):
        self.name = name
        self.date = date
        self.author = author
livros = []
livros.append(Livro("1984", 1960, "George Orwell"))
livros.append(Livro("A revolução dos bichos", 1945, "George Orwell"))
livros.append(Livro("Morro dos ventos uivantes", 1847, "Emily Brontë"))

while True:
    entrada = input("O que deseja fazer? \n " 
    "1 - Cadastrar livros \n " 
    "2 - Listar livros \n " 
    "3 - Buscar livros \n "
    "4 - Remover livros \n " 
    "0 - Sair \n ")

    if entrada == "1": #Parte de cadastrar livros
        while True:
            fechar = True
            try:
                objeto = Livro(input("Digite o nome do livro "), int(input("Digite a data do livro ")), input("Digite o autor do livro "))
                livros.append(objeto)
                print("Livro cadastrado! ")
            except:
                print("Entrada inválida")
                break
            while True:
                valor = input("O que deseja fazer agora? \n"
                "1 - Cadastrar outro livro \n"
                "0 - Voltar ao menu principal \n")
                if valor == "1":
                    break
                elif valor == "0":
                    fechar = False
                    break
                else:
                    print("Valor inválido. Por favor, tente de novo ")
            if fechar == False:
                break    
    elif entrada == "2": #Parte de listar os livros
        for i in livros:
            print(i.name)

    elif entrada == "3": #Parte de buscar os livros
        x = input("Qual livro deseja procurar? ")
        i = 0
        while i < len(livros):
            y = livros[i]
            if x == str(y.name):
                print ("Seu livro está aqui")
                break
            if i == int(len(livros)) - 1:
                print("Seu livro não está aqui")
            i = i + 1

    elif entrada == "4": #Parte de remover os livros
        print ("Escolha o livro q quer remover (0 se refere ao primeiro livro, 1 se refere ao segundo e assim por diante): ")
        for i in livros:
            print(i.name)
        try:
            z = int(input())
            if z in range(0, len(livros)):
                del livros[z]
                print("Livro removido!")
            else:
                print("Valor inválido, tente novamente")
        except:
            print("Entrada inválida, não foi possível verificar a solicitação")
            

    elif entrada == "0": #Parte de sair do programa
        break
    else:
        print("Valor inválido, por favor tente de novo")