d = {}
n = int(input())
for i in range(n):
    objs = input().split()
    if objs[1] in d:
        d[objs[1]] += 1
    else:
        d[objs[1]] = 1

h = {}
m = int(input())
for i in range(m):
    objs = input().split()
    if objs[1] in h:
        h[objs[1]] += int(objs[2])
    else:
        h[objs[1]] = int(objs[2])

for w in d:
    if w in h:
        if d[w] > h[w]: d[w] -= h[w]
        else: d[w] = 0

res = 0

for w in d:
    res += d[w]

print("Demons left: " + str(res))