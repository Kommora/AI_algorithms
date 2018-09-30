import pandas as pd
import numpy as np

base = pd.read_csv("/home/erik/PycharmProjects/algoritimos/car/car.data")


def count(ty,tx,x):
    y=[]
    cy=[]
    cyy=[]
    qtdc=[]
    if ty=="buying" or ty=="maint":
        y=["vhigh", "high", "med", "low"]
        cyy = [0, 0, 0, 0]
        qtdc = [0, 0, 0, 0]
    if ty=="doors":
        y=["2", "3", "4","5more"]
        cyy = [0, 0, 0, 0]
        qtdc = [0, 0, 0, 0]
    if ty=="persons":
        y=["2", "4", "more"]
        cyy = [0, 0, 0, 0]
        qtdc = [0, 0, 0, 0]
    if ty=="lug_boot":
        y=["small", "med", "big"]
        cyy = [0, 0, 0]
        qtdc = [0, 0, 0]
    if ty=="safety":
        y=["low", "med", "high"]
        cyy = [0, 0, 0]#p(y,x):y
        qtdc = [0, 0, 0]#p(y,x):x
    px=py=0

    for i in range(0,len(y)):
        for j in range(0,len(base)):
            if base.iloc[j][ty]==y[i]:
                px=px+1
        cy.append(px)
        px = 0

    for j in range(0,len(base)):
        if base.iloc[j][tx]==x:
            py=py+1
            
    for k in range(0,len(y)):
        for l in range(0,len(base)):
            if base.iloc[l][ty]==y[k]:
                qtdc[k]=qtdc[k]+1
            if base.iloc[l][tx]==x and base.iloc[l][ty]==y[k]:
                cyy[k]=cyy[k]+1

    for m in range(0,len(cyy)):
        cyy[m]=(((cyy[m])/qtdc[m])*((cy[m])/len(base)))/((py)/len(base))
    return cyy

print(count("lug_boot","doors","4"))