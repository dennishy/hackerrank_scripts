import textwrap

def wrap(string, max_width):

    a = [] 
  
    if len(string) < max_width:
        pass 
    else:
        y = len(string) // max_width 
        i = 0 
        mw = max_width
        while i <= y:   
            a.append(string[i*max_width:(i*max_width)+max_width])
            i+=1
    return '\n'.join([str(i) for i in a])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)