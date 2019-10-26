
def doormat(n,m):
    #m is always 3x n 

    #n is rows, m is columns 

    pattern = '.|.'
     
    for i in range(n):
        if i%2!=0:
            print('{:-^0{width}}'.format(pattern*i, width=m))

    print('{:-^0{width}}'.format('WELCOME', width=m))

    for i in range(n):
        if i%2!=0:
            print('{:-^0{width}}'.format(pattern*(n-1-i), width=m))

if __name__ == '__main__':
    n,m = [int(x) for x in input().split()]

    doormat(n,m)
   