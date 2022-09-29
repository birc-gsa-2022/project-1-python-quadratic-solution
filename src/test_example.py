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

def test_files():
    makeFile(fastaGenerator(), fileName="test.fa")
    makeFile(fastqGenerator(seqlen=5), fileName="test.fq")

def compare_res(x, p, *algorithms):
    res = [list(a(x,p)) for a in algorithms]
    for i in range(1, len(res)):
        assert len(res[0]) == len(res[i]), f"Not same len for {algorithms[0].__name__} and {algorithms[i].__name__} with input {x} and {p}"
    for i in range(1, len(res)):
        assert res[0] == res[i], f"Not same output for {algorithms[0].__name__()} and {algorithms[i].__name__()} with input {x} and {p}"

def test_defined():
    x = ""
    p = ""
    compare_res(x, p, naive.naive, naive.naive2, lin.bmh, lin.kmp, lin.kmp2)

    x = "mississippi"
    p = "ssi" 
    compare_res(x, p, naive.naive, naive.naive2, lin.bmh, lin.kmp, lin.kmp2)

    x = "aaaaa"
    p = "aa"
    compare_res(x, p, naive.naive, naive.naive2, lin.bmh, lin.kmp, lin.kmp2)

    x = "gtccccacatcct"
    p = "ccc"
    compare_res(x, p, naive.naive, naive.naive2, lin.bmh, lin.kmp, lin.kmp2)


def test_random_same():
    setSeed()
    for i in range(500):
        x= "".join(r.choices(genAlphabet, k=i))
        for j in range(50, i+2):
            pat = "".join(r.choices(genAlphabet, k=j))
            compare_res(x, pat, naive.naive, naive.naive2, lin.bmh, lin.kmp, lin.kmp2)

def test_naive2():
    x = ["aaaaa", "mississippi","", "aaabc","abc","a b c", "abababbababa", "Genome"]
    p = ["aa", "iss","","bc", "abcd", "b ", "ba", "good grades"]
    expected = [[0,1,2,3],[1,4],[],[3],[],[2],[1,3,6,8,10], []]

    for i in range(len(x)):
        res = naive.naive2(x[i],p[i])
        assert list(res) == expected[i]

def test_naive():
    x = ["aaaaa", "mississippi","", "aaabc","abc","a b c", "abababbababa", "Genome"]
    p = ["aa", "iss","","bc", "abcd", "b ", "ba", "good grades"]
    expected = [[0,1,2,3],[1,4],[],[3],[],[2],[1,3,6,8,10], []]

    for i in range(len(x)):
        res = naive.naive(x[i],p[i])
        assert list(res) == expected[i]

def test_kmp():
    x = ["aaaaa", "mississippi","", "aaabc","abc","a b c", "abababbababa", "Genome", "abxabxabx", "abxabdabx", "bcagjkdasbca"]
    p = ["aa", "iss","","bc", "abcd", "b ", "ba", "good grades", "abc", "abx", "a"]
    expected = [[0,1,2,3],[1,4],[],[3],[],[2],[1,3,6,8,10], [], [],[0,6],[2,7,11]]

    for i in range(len(x)):
        res = lin.kmp(x[i],p[i])
        assert list(res) == expected[i]

def test_kmp2():
    x = ["aaaaa", "mississippi","", "aaabc","abc","a b c", "abababbababa", "Genome", "abxabxabx", "abxabdabx", "bcagjkdasbca"]
    p = ["aa", "iss","","bc", "abcd", "b ", "ba", "good grades", "abc", "abx", "a"]
    expected = [[0,1,2,3],[1,4],[],[3],[],[2],[1,3,6,8,10], [], [],[0,6],[2,7,11]]

    for i in range(len(x)):
        res = lin.kmp2(x[i],p[i])
        assert list(res) == expected[i]

def test_bmh():
    x = ["aaaaa", "mississippi","", "aaabc","abc","a b c", "abababbababa", "Genome", "abxabxabx", "abxabdabx", "bcagjkdasbca"]
    p = ["aa", "iss","","bc", "abcd", "b ", "ba", "good grades", "abc", "abx", "a"]
    expected = [[0,1,2,3],[1,4],[],[3],[],[2],[1,3,6,8,10], [], [],[0,6],[2,7,11]]

    for i in range(len(x)):
        res = lin.bmh(x[i],p[i])
        assert list(res) == expected[i]