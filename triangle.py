import math 

ab = int(input())
bc = int(input())

out = math.degrees(math.atan2(ab, bc))

print('{}°'.format(round(out)))
