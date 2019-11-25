print("digite o que deseja fazer: " )
index = input("\n" +"1 - adicionar notas" +
              "\n" + "2 - calcular média" +
              "\n" + "3 - alterar nota" +
              "\n" + "4 - adicionar mais uma nota" +
              "\n" + "5 - ver situação do aluno" +
              "\n" + "6 - mostrar todas as notas" +
              "\n" + "7 - sair" +
              "\n"
              )

boletim = {}

while index != "7":

#adicionar notas e alunos
    if index == "1":
        qtdAlunos = int(input("digite a quantidade de alunos que deseja adicionar as notas: "))
        qtdNotas = int(input("digite a quantidade de notas que deseja adicionar para os alunos"))
        for i in range(qtdAlunos):
            print()
            nomeAluno = input("digite o nome do aluno: ").upper()
            notas = []
            for x in range(qtdNotas):
                notasAlunos = float(input("digite a nota de "+nomeAluno+": "))
                notas.append(notasAlunos)
            boletim[nomeAluno] = notas
        print()
        print("notas registradas com sucesso!")
        print()
        print(boletim)
    print()

    print("digite o que deseja fazer: ")
    index = input("\n" + "1 - adicionar notas" +
                  "\n" + "2 - calcular média" +
                  "\n" + "3 - alterar nota" +
                  "\n" + "4 - adicionar mais uma nota" +
                  "\n" + "5 - ver situação do aluno" +
                  "\n" + "6 - mostrar todas as notas" +
                  "\n" + "7 - sair" +
                  "\n"
                  )

#calcular média do aluno
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
            print()
            print("o aluno não está cadastrado")

#alterar nota do aluno
    if index == "3":
        print()
        print(boletim)
        print()
        editarNotaAluno = input("digite o nome do aluno que deseja editar as notas: ").upper()
        if editarNotaAluno in boletim.keys():
            print()
            print(boletim[editarNotaAluno])
            print()
            notaExistente = float(input("digite a nota de "+editarNotaAluno+" que deseja alterar: "))
            if notaExistente in boletim[editarNotaAluno]:
                novaNota = float(input("digite a nova nota para "+editarNotaAluno+": "))
                boletim[editarNotaAluno].remove(notaExistente)
                boletim[editarNotaAluno].append(novaNota)
                print()
                print("nota alterada com sucesso!")
            else:
                print("a nota que foi inserida não está cadastrada")
        else:
            print(editarNotaAluno+" não está cadastrado")
        print()
        print(boletim)



#adicionar mais notas
    if index == "4":
        print()
        print(boletim)
        print()
        inserirNotaAluno = input("digite o nome do aluno no qual deseja adicionar mais uma  nota: ").upper()
        print()
        if inserirNotaAluno in boletim.keys():
            qtdNovaNota =  int(input("digite quantas notas deseja adicionar a "+inserirNotaAluno+ " :"))
            for l in range(qtdNovaNota):
                addNovaNota = float(input("insira a nota que deseja adicionar para "+ inserirNotaAluno+ " :"))
                notas.append(addNovaNota)
            print()
            print("nota adicionada com sucesso!")
            print(boletim)
        else:
            print(inserirNotaAluno+" não está cadastrado")
#ver situação do aluno
    if index == "5":
        print()
        print(boletim)
        print()
        situacaoAluno = input("digite o nome do aluno que deseja ver a situação: ").upper()
        if situacaoAluno in boletim.keys():
            notas = boletim[situacaoAluno]
            mediaFinal = sum(notas)/len(notas)
            #medias.append(mediaFinal)
            if mediaFinal >= 7:
                print()
                print(situacaoAluno+" foi aprovado")
                print("notas: ",boletim[situacaoAluno])
                print("média final: ",mediaFinal)
            else:
                print()
                print(situacaoAluno+" foi reprovado")
                print("notas: ", boletim[situacaoAluno])
                print("média final: ",mediaFinal)
        else:
            print()
            print(situacaoAluno+" não está cadastrado")


#mostrartodo o boletim
    if index == "6":
        for i in boletim.keys():
            print()
            notas = boletim[i]
            mediaFinal = sum(notas) / len(notas)
            print('aluno: {} , notas: {} , media final: {}'.format(i,boletim[i], mediaFinal))

print()
print("obrigada por utilizar o sistema!")