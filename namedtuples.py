from collections import namedtuple


(n, c) = (int(input()), input().split())

scores = namedtuple('scores', c)
marks = [int(scores._make(input().split()).MARKS) for _ in range(n)]

print('{0:.2f}'.format(sum(marks)/len(marks)))