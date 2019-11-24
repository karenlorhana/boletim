index = input("digite o que deseja fazer: " +
              "\n"+"1 - adicionar notas" +
              "\n"+"2 - calcular média" +
              "\n"+"3 - alterar nota" +
              "\n"+"4 - ver situação do aluno"
              "\n"+"5 - sair"+
              "\n"
              )

boletim = {}

while index != "4":
    if index == "1":
        qtdAlunos = int(input("digite a quantidade de alunos que deseja adicionar as notas: "))
        for i in range(qtdAlunos):
            print()
            nomeAluno = input("digite o nome do aluno: ").upper()
            notas = []
            for x in range(2):
                notasAlunos = float(input("digite a nota de "+nomeAluno+": "))
                notas.append(notasAlunos)
            boletim[nomeAluno] = notas
        print()
        print(boletim)
    print()
    index = input("digite o que deseja fazer: " +
                  "\n" + "1 - adicionar notas" +
                  "\n" + "2 - calcular média" +
                  "\n" + "3 - alterar nota" +
                  "\n" + "4 - ver situação do aluno"
                  "\n" + "5 - sair" +
                  "\n"
                  )

    if index == "2":
        print()
        print(boletim)
        print()
        buscarAluno = input("digite o nome do aluno que deseja calcular a média: ").upper()
        if buscarAluno in boletim.keys():
            notas = boletim[buscarAluno]
            media = sum(notas)/len(notas)
            print()
            print("a média de "+buscarAluno+" é: ", media)

    if index == "3":
        print()
        print(boletim)
        print()
        editarNotaAluno = input("digite o nome do aluno que deseja editar as notas: ").upper()
        if editarNotaAluno in boletim.keys():
            for i in range(2):
                novaNota = float(input("digite a nova nota para "+editarNotaAluno+": "))
                boletim[editarNotaAluno].append(novaNota)
        boletim[editarNotaAluno].pop(0)
        boletim[editarNotaAluno].pop(0)
        print()
        print(boletim)

    if index == "4":
        situacaoAluno = input("digite o nome do aluno que deseja ver a situação: ").upper()
        if situacaoAluno in boletim.keys():
            notas = boletim[situacaoAluno]
            mediaFinal = sum(notas)/len(notas)
            if mediaFinal > 7:
                print(situacaoAluno+" foi aprovado")
                print(boletim[situacaoAluno])
            else:
                print(situacaoAluno+" foi reprovado")
                print(boletim[situacaoAluno])