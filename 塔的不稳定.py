
a = input().split()
#塔的数量以及最多操作的次数
b = int(a[0])
c = int(a[1])
m = [int(i) for i in input().split()]
#每座塔得初始高度
d = {}
for j in range(1,b+1):
    d[j] = m[j-1]
e = sorted(d.items(), key=lambda d:d[1])
f = []
g = []
for i in range(c):
    d[e[0][0]]= e[0][1] + 1
    d[e[-1][0]] = e[-1][1] - 1
    f.append([e[-1][0],e[0][0]])
    e = sorted(d.items(), key=lambda d: d[1])
    g.append([e[-1][1]-e[0][1], i+1])
minv = [i for i in g if i[0] == min([j[0] for j in g])]
print(minv[0][0],end=' ')
print(minv[0][1])
for j in range(minv[0][1]):
    print(f[j][0], end=' ')
    print(f[j][1])





