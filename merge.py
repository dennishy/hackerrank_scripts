def merge_the_tools(string, k):
    loops = int(len(string)/k)

    for i in range(loops):
        b = i * k
        print(string[b:b+3]) 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)