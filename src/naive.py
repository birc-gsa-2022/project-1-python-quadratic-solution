"""Implementation of the naive exact matching algorithm."""

import argparse
import parser as p 


def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching using the naive method")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()
    # print(f"Find every reads in {args.reads.name} " +
    #       f"in genome {args.genome.name}")
    fasta = p.parseFasta(args.genome)
    fastq = p.parseFastq(args.reads)
    for (fastaName, fastaSeq) in fasta:
        for (name,seq) in fastq:
            for i in naive2(fastaSeq, seq):
                print(name, fastaName, i+1, f'{len(seq)}M', seq, sep="\t")


def naive(x, p):
    upperIndex = len(x)-len(p)+1
    for i in range(upperIndex):
        for j, patternchar in enumerate(p):
            if x[i+j] != patternchar:
                break
        else:
            yield i

def naive2(x,p):
    m = len(p)
    upperIndex = len(x)-m+1
    for i in range(upperIndex):
        if x[i:i+m] == p: #python is bail out fast
            yield i


if __name__ == '__main__':
    main()
