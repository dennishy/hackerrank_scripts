clouds = 7 
cloud_map = list(map(int,'0 0 1 0 0 1 0'.split()))

jumps = 0

i = 0 


while i < clouds-1:
    if i <= clouds - 3 and cloud_map[i+2] == 0:
        i += 2
        jumps += 1
    else:
        i += 1
        jumps +=1

        
    print('jump num: {} and jump value: {}'.format(str(i), str(jumps)))
