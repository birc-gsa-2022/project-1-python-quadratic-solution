import timer as t
import naive as n
import lin
import test_example
import parser
import random as r
import pandas as pd

#TODO less variation of m. NO iterations. more variation of n


timer = t.Clock()
numIterations = 50
alphabet = "acgt"
seqlen = 1000000
patlen = 10000

data = dict()

lseq = []
lpat = []
lnaive = []
lnaive2 = []
lkmp = []
lkmp2 = []
lbmh = []

for patLen in range(1000,patlen+1, 1000):
    print("New pattern len is :", patLen)
    for seqLen in range(100000, seqlen+1, 100000):
        for i in range(numIterations):
            seq = "".join(r.choices(alphabet, k=seqLen))
            pat = "".join(r.choices(alphabet, k=patLen)) 
            naive = timer.timeAlgorithm(n.naive,seq, pat)
            naive2 = timer.timeAlgorithm(n.naive2,seq, pat)
            kmp = timer.timeAlgorithm(lin.kmp,seq, pat)
            kmp2 = timer.timeAlgorithm(lin.kmp2,seq, pat)
            bmh = timer.timeAlgorithm(lin.bmh,seq, pat)
            lseq.append(len(seq))
            lpat.append(len(pat))
            lnaive.append(naive)
            lnaive2.append(naive2)
            lkmp.append(kmp)
            lkmp2.append(kmp2)
            lbmh.append(bmh)


data['seq'] = lseq
data['pat'] = lpat
data['naive'] = lnaive
data['naive2'] = lnaive2
data['kmp'] = lkmp
data['kmp2'] = lkmp2
data['bmh'] = lbmh

dataframe = pd.DataFrame(data)

dataframe.to_csv("data2.csv", index=False)
