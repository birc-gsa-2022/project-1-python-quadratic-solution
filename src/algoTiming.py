import timer as t
import naive as n
import lin
import random as r
import pandas as pd
import numpy as np

timer = t.Clock()
numIterations = 100
numAvgIterations = 5
alphabet = "acgt"
seqlen = 1000000
patlen = 3000

data = dict()

lseq = []
lpat1 = []
lpat2 = []
lpat3 = []

lnaive1 = []
lnaive2 = []
lnaive3 = []

lkmp1 = []
lkmp2 = []
lkmp3 = []

#We generate a new seqeunce to look through before a run of an algorithm 
#This is done to minizime the amout knowlegde python has of the seqence before running each algorithm  

for seqLen in range(100000, seqlen+1, 10000):
    print("Seq len is now:",seqLen)
    tempNaive1 = []
    tempKmp1 = []
    tempNaive2 = []
    tempKmp2 = []
    tempNaive3 = []
    tempKmp3 = []
    for _ in range(numIterations):
        seq = "".join(r.choices(alphabet, k=seqLen))
        pat1 = "".join(r.choices(alphabet, k=100)) 
        naive1 = timer.getAverageTime(numAvgIterations, n.naive2,seq, pat1)
        tempNaive1.append(naive1)
        seq = "".join(r.choices(alphabet, k=seqLen))
        kmp1 = timer.getAverageTime(numAvgIterations,lin.kmp2,seq, pat1)
        tempKmp1.append(kmp1)
    
        pat2 = "".join(r.choices(alphabet, k=1000))
        seq = "".join(r.choices(alphabet, k=seqLen))
        naive2 = timer.getAverageTime(numAvgIterations, n.naive2,seq, pat2)
        tempNaive2.append(naive2)
        seq = "".join(r.choices(alphabet, k=seqLen))
        kmp2 = timer.getAverageTime(numAvgIterations, lin.kmp2,seq, pat2)
        tempKmp2.append(kmp2)
        
        seq = "".join(r.choices(alphabet, k=seqLen))
        pat3 = "".join(r.choices(alphabet, k=10000))
        naive3 = timer.getAverageTime(numAvgIterations, n.naive2,seq, pat3)
        tempNaive3.append(naive3)
        seq = "".join(r.choices(alphabet, k=seqLen))
        kmp3 = timer.getAverageTime(numAvgIterations, lin.kmp2,seq, pat3)
        tempKmp3.append(kmp3)

    lseq.append(seqLen)
    #lpat1.append(len(pat1))
    #lpat2.append(len(pat2))
    #lpat3.append(len(pat3))
    
    lnaive1.append(np.average(tempNaive1))
    lkmp1.append(np.average(tempKmp1))
    lnaive2.append(np.average(tempNaive2))
    lkmp2.append(np.average(tempKmp2))
    lnaive3.append(np.average(tempNaive3))
    lkmp3.append(np.average(tempKmp3))


data['seq'] = lseq
#data['pat1'] = lpat1
#data['pat2'] = lpat2
#data['pat3'] = lpat3

data['naive1'] = lnaive1
data['naive2'] = lnaive2
data['naive3'] = lnaive3

data['kmp1'] = lkmp1
data['kmp2'] = lkmp2
data['kmp3'] = lkmp3

dataframe = pd.DataFrame(data)

dataframe.to_csv("data3.csv", index=False)
