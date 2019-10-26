from collections import Counter
import itertools


def minion_game(string):
    vowels = 'AEIOU'
    ksco = 0
    ssco = 0
    
    wordLength = len(string)

    for i in range(wordLength):
        if string[i] in vowels:
            ksco += wordLength - i
        else:
            ssco += wordLength - i

    if ksco == ssco:
        print('Draw')
    elif ksco > ssco:
        print('Kevin '+str(ksco))
    else:
        print('Stuart '+str(ssco))





'''
    words = [string[i:j] for i in range(len(string)) 
                for j in range(i + 1, len(string) + 1)]
      

    v = Counter()
    c = Counter()

    for word in words:
        if word[0] in vowels:
            v[word]+=1
        else:
            c[word]+=1

    v_sum =sum(v.values())
    c_sum =sum(c.values())

    if v_sum == c_sum:
        print('Draw')
    elif v_sum > c_sum:
        print('Kevin '+str(v_sum))
    else:
        print('Stuart '+str(c_sum))

'''
if __name__ == '__main__':
    s = input()
    minion_game(s)

