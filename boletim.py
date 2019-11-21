index = input("digite o que deseja fazer: " +
              "\n"+"1 - adicionar notas" +
              "\n"+"2 - calcular média" +
              "\n"+"3 - alterar nota" +
              "\n"+"4 - sair"
              )

boletim = {}

while index != "4":
    if index == "1":
        qtdAlunos = int(input("digite a quantidade de alunos que deseja adicionar as notas: "))
        for i in range(qtdAlunos):
            nomeAluno = input("digite o nome do aluno: ").upper()
            notas = []
            for x in range(2):
                notasAlunos = int(input("digite a nota de "+nomeAluno+": "))
                notas.append(notasAlunos)
            boletim[nomeAluno] = notas
        print(boletim)

    index = input("digite o que deseja fazer: " +
                  "\n" + "1 - adicionar notas" +
                  "\n" + "2 - calcular média" +
                  "\n" + "3 - alterar nota" +
                  "\n" + "4 - sair"
                  )

    if index == "2":
        print(boletim)
        buscarAluno = input("digite o nome do aluno que deseja calcular a média: ").upper()
        if buscarAluno in boletim.keys():
            notas = boletim[buscarAluno]
            media = sum(notas)/len(notas)
            print("a média de "+buscarAluno+" é: ", media)

    if index == "3":
        print(boletim)
        editarNotaAluno = input("digite o nome do aluno que deseja editar as notas: ").upper()
        if editarNotaAluno in boletim.keys():
            for i in range(2):
                novaNota = int(input("digite a nova nota para "+editarNotaAluno+": "))
                boletim[editarNotaAluno].append(novaNota)
        boletim[editarNotaAluno].pop(0)
        boletim[editarNotaAluno].pop(0)
        print(boletim)
