index = input("digite o que deseja fazer: " +
              "\n"+"1 - adicionar notas" +
              "\n"+"2 - calcular média" +
              "\n"+"3 - alterar nota" +
              "\n"+"4 - ver situação do aluno"+
              "\n"+"5 - mostrar todas as notas" +
              "\n"+"6 - sair"+
              "\n"
              )

boletim = {}

while index != "6":
    if index == "1":
        qtdAlunos = int(input("digite a quantidade de alunos que deseja adicionar as notas: "))
        qtdNotas = int(input("digite a quantidade de notas que deseja adicionar para os alunos"))

        for i in range(qtdAlunos):
            print()
            nomeAluno = input("digite o nome do aluno: ").upper()
            notas = []
            #medias = []
            for x in range(qtdNotas):
                notasAlunos = float(input("digite a nota de "+nomeAluno+": "))
                notas.append(notasAlunos)
            boletim[nomeAluno] = notas
            #boletim[nomeAluno] = medias
        print()
        print(boletim)
    print()
    index = input("digite o que deseja fazer: " +
                  "\n" + "1 - adicionar notas" +
                  "\n" + "2 - calcular média" +
                  "\n" + "3 - alterar nota" +
                  "\n" + "4 - ver situação do aluno"
                  "\n" + "5 - mostrar todas as notas" +
                  "\n" + "6 - sair" +
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
        else:
            print("o aluno não está cadastrado")

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
        print()
        print(boletim)
        print()
        situacaoAluno = input("digite o nome do aluno que deseja ver a situação: ").upper()
        if situacaoAluno in boletim.keys():
            notas = boletim[situacaoAluno]
            mediaFinal = sum(notas)/len(notas)
            #medias.append(mediaFinal)
            if mediaFinal >= 7:
                print(situacaoAluno+" foi aprovado")
                print(boletim[situacaoAluno])
                print("média final: ",mediaFinal)
            else:
                print(situacaoAluno+" foi reprovado")
                print(boletim[situacaoAluno])
                print("média final: ",mediaFinal)
        else:
            print("o aluno não está cadastrado")
    if index == "5":
        print(boletim)