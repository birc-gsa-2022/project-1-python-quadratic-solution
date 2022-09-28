# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
import random as r
import lin 
import naive

genAlphabet = "acgt"

def setSeed(seed=None):
    if seed == None:
        seed = r.randint(0,1000)
    with open("seed.txt", "a") as f:
        f.write(f"Last seed was {seed} \n" )
    r.seed(seed)

def fastaGenerator(seqlen=1000, alphabet=genAlphabet):
    name = "".join(r.choices(alphabet, k=r.randint(1, 10)))
    seq = "".join(r.choices(alphabet, k=seqlen))
    return f">{name}\n{seq}"

def fastqGenerator(num=0, seqlen=10, alphabet=genAlphabet):
    seq = "".join(r.choices(alphabet, k=seqlen))    
    return f"@read{num}\n{seq}"

def makeFile(string, fileName="test"):
    with open(fileName, "a") as f:
        f.write(string+"\n")

makeFile(fastaGenerator(), fileName="test.fa")
makeFile(fastqGenerator(seqlen=3), fileName="test.fq")

string= "".join(r.choices(genAlphabet, k=1000))
pat = "".join(r.choices(genAlphabet, k=1))
nai = [n for n in naive.naive2(string, pat)]
li = [l for l in lin.kmp(string, pat)]

print("Length nai : " + str(len(nai)))
print("Length li : " + str(len(li)))

assert len(nai) == len(li)

for i in range(len(nai)):
    assert nai[i] == li[i]




def test_1984():
    assert 2 + 2 == 4
