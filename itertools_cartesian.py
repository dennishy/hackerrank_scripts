from itertools import product

if __name__=="__main__":
    
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    c = list(product(a,b))

    print(*c)
