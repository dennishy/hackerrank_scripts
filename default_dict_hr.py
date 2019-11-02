from collections import defaultdict

dd = defaultdict(list)

n, m = map(int, input().split())

for i in range(1, n+1):
    word = input()
    dd[word].append(i)

checklist = []
for j in range(m):
    checklist.append(input())

for checkword in checklist:
    if not dd[checkword]:
        print(-1)
    else:
        print(' '.join([str(k) for k in dd[checkword]]))
    