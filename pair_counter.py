from collections import Counter
def idk(n, test):
    v = Counter(test)
    paircount = 0

    for key in v:
        if v[key] // 2 > 0:
            paircount += 1
    return(paircount)

n = 5
test = '10 10 20 20 30'

test = list(map(int, test.split()))

print(idk(5, test))
