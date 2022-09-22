"""Implementation of a linear time exact matching algorithm."""

import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching in linear time")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()
    print(f"Find every reads in {args.reads.name} " +
          f"in genome {args.genome.name}")


def border_array(x: str) -> list[int]:
    """
    Construct the border array for x.

    >>> border_array("aaba")
    [0, 1, 0, 1]
    >>> border_array("ississippi")
    [0, 0, 0, 1, 2, 3, 4, 0, 0, 1]
    >>> border_array("")
    []
    """
    ba = []

    for i, char in enumerate(x):
        j = i 
        while True:
            if j == 0:
                ba.append(0)
                break
            baPrev = ba[j-1]
            if x[baPrev] == char:
                ba.append(baPrev+1)
                break
            j = baPrev 
    return ba

def strict_border_array(x: str) -> list[int]:
    """
    Construct the strict border array for x.

    A struct border array is one where the border cannot
    match on the next character. If b is the length of the
    longest border for x[:i+1], it means x[:b] == x[i-b:i+1],
    but for a strict border, it must be the longest border
    such that x[b] != x[i+1].

    >>> strict_border_array("aaba")
    [0, 1, 0, 1]
    >>> strict_border_array("aaaba")
    [0, 0, 2, 0, 1]
    >>> strict_border_array("ississippi")
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 1]
    >>> strict_border_array("")
    []
    """
    ba = border_array(x)
    for i, bai in enumerate(ba[:-1]):
        if bai != 0 and x[i+1] == x[bai]:
            ba[i]= ba[bai-1]  
    return ba

#Not working
#TODO make not go trough when pattern is bigger 
#FIXME fix when m=1 
def kmp(x, p):
    ba = strict_border_array(p)
    m = len(p)
    n = len(x)
    i = 0
    j = 0
    while j < n:
        if x[j] == p[i]:
            if i==m-1:
                i = max(0, ba[i-1]) #Technically not needed? 
                yield j-i
            else:
                j += 1
                i += 1
        elif i==0:
            j += 1
        else:
            i = ba[i-1]
            



if __name__ == '__main__':
    main()
