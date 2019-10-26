def solve(s):
    names = s.split(' ')

    names2 = [x.capitalize() for x in names]
    print(' '.join(names2))
 



if __name__ == '__main__':

    s = input()
    solve(s)

