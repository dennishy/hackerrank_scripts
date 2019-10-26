def swap_case(s):

    b = ''

    for a in s:
        if a.isupper():
            b += a.lower()
        else:
            b += a.upper()
    return b

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)