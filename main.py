# -*- coding: utf-8 -*-

arquivo = open("gramatica.txt","r")

gramatica = arquivo.readlines()

gramaticaDesmontada = []
first = {}
follow = {}

for linha in gramatica:
    linha = linha.replace(" ", "").replace("-", "|").replace("\n", "")
    linhaExplodida = linha.split("|")
    first[linhaExplodida[0]] = ""
    follow[linhaExplodida[0]] = ""
    gramaticaDesmontada.append(linha)

follow[gramaticaDesmontada[0][0]] = "$"

contador = 0


def acharFirst(gramaticaDesmontada, first):
    for i in range(0, len(gramaticaDesmontada)):
        linhaExplodida = gramaticaDesmontada[i].split("|")
        cont = len(linhaExplodida)
        for j in range(1, len(linhaExplodida)):
            possuiNaoTerminal = False
            for caracter in linhaExplodida[j]:
                if caracter.isupper():
                    possuiNaoTerminal = True
            if possuiNaoTerminal:
                first[linhaExplodida[0]] = first[linhaExplodida[0]] + "," + linhaExplodida[j][0]
            else:
                first[linhaExplodida[0]] = first[linhaExplodida[0]] + "," + linhaExplodida[j]

    for novaLinha in first:
        first[novaLinha] = first[novaLinha][1:len(first[novaLinha])]

    return first


def eliminarNaoTerminais(first):
    possuiNaoTerminais = True
    while possuiNaoTerminais:
        for linha in first:
            for caracter in first[linha].split(","):
                if caracter.isupper():
                    if linha != caracter:
                        for outroCaracter in first[caracter].split(","):
                            existeCaracter = False
                            for caracterLinha in first[linha].split(","):
                                if caracterLinha == outroCaracter:
                                    existeCaracter = True

                            if not existeCaracter:
                                first[linha] = first[linha] + "," + outroCaracter

                        novoFirst = first[linha].replace(caracter + ",", '')
                        novoFirst = novoFirst.replace("," + caracter, '')
                        first[linha] = novoFirst
                    else:
                        novoFirst = first[linha].replace(caracter + ",", '')
                        novoFirst = novoFirst.replace("," + caracter, '')
                        first[linha] = novoFirst

        possuiNaoTerminais = False
        for linha2 in first:
            for caracteres in first[linha2]:
                if caracteres.isupper():
                    possuiNaoTerminais = True

    return first

def montarFollow(gramaticaDesmontada, follow, first):
    possuiNaoTerminais = True
    cont = 0
    while possuiNaoTerminais:
        for linha in follow:
            for linhaGramatica in gramaticaDesmontada:
                linhaGramaticaExplodida = linhaGramatica.split("|")
                for i in range(1, len(linhaGramaticaExplodida)):
                    if linhaGramaticaExplodida[i].find(linha) != -1:
                        if linhaGramaticaExplodida[i].find(linha) == len(linhaGramaticaExplodida[i])-1:
                            if linha != linhaGramaticaExplodida[0]:
                                if follow[linhaGramaticaExplodida[0]] == "":
                                    if follow[linha] != "":
                                        for caracter in follow[linhaGramaticaExplodida[0]]:
                                            if follow[linha].find(caracter) == -1:
                                                follow[linha] = follow[linha] + linhaGramaticaExplodida[0]
                                    else:
                                        follow[linha] = follow[linha] + linhaGramaticaExplodida[0]
                                else:
                                    for caracter in follow[linhaGramaticaExplodida[0]]:
                                        if follow[linha].find(caracter) == -1:
                                            follow[linha] = follow[linha] + caracter

                                    follow[linha] = follow[linha].replace(linhaGramaticaExplodida[0], "")
                        else:
                            if linhaGramaticaExplodida[i][linhaGramaticaExplodida[i].find(linha)+1].isupper():
                                for caracter in first[linhaGramaticaExplodida[i][linhaGramaticaExplodida[i].find(linha)+1]].split(","):
                                        if follow[linha].find(caracter) == -1:
                                            follow[linha] = follow[linha] + caracter
                                follow[linha] = follow[linha].replace("&", "")
                            else:
                                if follow[linha].find(linhaGramaticaExplodida[i][linhaGramaticaExplodida[i].find(linha)+1]) == -1:
                                            follow[linha] = follow[linha] + linhaGramaticaExplodida[i][linhaGramaticaExplodida[i].find(linha)+1]

        possuiNaoTerminais = False
        for linha2 in follow:
            for caracteres in follow[linha2]:
                if caracteres.isupper():
                    if cont < 2:
                        possuiNaoTerminais = True
                    else:
                        follow[linha2] = follow[linha2].replace(caracteres, "")
        cont = cont + 1

    return follow

first = acharFirst(gramaticaDesmontada, first)
first = eliminarNaoTerminais(first)
follow = montarFollow(gramaticaDesmontada, follow, first)

print first
print follow