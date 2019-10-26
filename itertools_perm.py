from itertools import permutations

if __name__=='__main__':
    s, k = input().split()

    s = list(s)
    s.sort()

    k = int(k)

    p = list(permutations(s,k))

    for x in p:
        test = ''.join(x)
        print(test)
