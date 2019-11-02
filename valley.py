#steps
n = 8

#path
s = 'UDDDUDUU'

height = 0
valley = 0 
peak = 0

step_dict = dict()

for step in range(n):
    if s[step] == 'U':
        height += 1
    else: 
        height -=1

    step_dict[step] = height

    if step == 0:
        next
    elif step_dict[step] == 0:
        if step_dict[step-1] > 0:
            peak += 1
        else:
            valley += 1



print(valley)