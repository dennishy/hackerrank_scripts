import math

def sdev(n,m):
    mean = sum([x for x in m])/n

    a = 0
    for x in m:
        a += (x - mean)**2

    a = a / n
    return math.sqrt(a)

if __name__=='__main__':
    n = int(input())
    m = [int(x) for x in input().split()]

    print('{0:.1f}'.format(sdev(n,m))) 