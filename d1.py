#test1 = 9
#test2 = '3 7 8 5 12 14 21 13 18'



def median(x):
    l = len(x)

    if l % 2 == 0:
        m1 = l // 2 
        m2 = (l // 2) - 1 

        m = (x[m1] + x[m2])//2

    else:
        m = int(round(l/2))
        m = x[m]

    return(m)

if __name__ == '__main__':

    k = int(input())
    x = sorted(list(map(int, input().split() )))


    print(median(x[:k//2]))
    print(median(x))
    print(median(x[(k+1)//2:]))
    