def distinct_letters(x):
    hold = [] 

    for a in x:
        if a not in hold:
            hold += a
        else:
            next

    return ''.join([a for a in hold])


def merge_the_tools(string, k):

    letter = []

    for i in range(0,len(string),k):
        start = i
        end = i+k
    
        letter = string[start:end]
        print(distinct_letters(letter))


if __name__ == '__main__':
#    string, k = input(), int(input())
#    merge_the_tools(string, k)

    merge_the_tools('AABCAAADA',3)