import pandas as pd
import operator as op
import random

data = pd.read_csv("/home/erik/PycharmProjects/algoritimos/wine/wine.data")

def euclides(treino,teste):
    distancia=0
    for x in range(1,len(teste)):
        distancia = distancia + pow((teste[x]-treino[x]),2)
    return distancia**0.5

def vizinhos(treino,teste,k):
    distancias=[]
    for x in range(0,len(treino)):
        dist = euclides(treino[x],teste)
        distancias.append([dist,treino[x]])
    distancias.sort(key=op.itemgetter(0))
    vizinho=[]
    for x in range(k):
        vizinho.append(distancias[x][1])
    return vizinho


def dividir(treino,teste):
    for x in range(0,len(data)):
        for y in range(1,len(data.iloc[0])):
            if random.random()<0.75:
                treino.append(data.iloc[x])
            else:
                teste.append(data.iloc[x])
    return

def resposta(vizinhos):
    classeVotos = {}
    for x in range(1,len(vizinhos)):
        rspt = vizinhos[x][0]
        if rspt in classeVotos:
            classeVotos[rspt] += 1
        else:
            classeVotos[rspt] = 1
    VotosOrdenados = sorted(classeVotos.items(), key=op.itemgetter(1), reverse=True)
    return VotosOrdenados[0][0]


def acuracia(testSet, predicoes):
    certo = 0
    for x in range(0,len(testSet)):
        if testSet[x][0] == predicoes[x]:
            certo += 1
    return (certo / float(len(testSet))) * 100.0

treino=[]
teste=[]

dividir(treino,teste)

predicoes=[]

k=3
for x in range(len(teste)):
    vz=vizinhos(treino,teste[x],k)
    r = resposta(vz)
    predicoes.append(r)
    print("Predito:"+repr(r)+" atual:"+repr(teste[x][0]))
print(acuracia(teste,predicoes))
