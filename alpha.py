def rangoli(n):

    alpha = [chr(i+96) for i in range(1, n+1)]
    alpha.sort(reverse=True)
    
    patternCollection = []

    for i in range(1, n+1):

        pattern = '-'.join([x for x in alpha[:i]] + [x for x in alpha[:i-1][::-1]])

        patternCollection.append(pattern)

    width = len(patternCollection[-1])


    for x in patternCollection:
        print('{0:-^{width}}'.format(x, width=width))

    for x in patternCollection[:-1][::-1]:
        print('{0:-^{width}}'.format(x, width=width))


if __name__=='__main__':
    n = int(input())
    
    rangoli(n)