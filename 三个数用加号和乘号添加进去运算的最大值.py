a = [int(i) for i in input().split()]
a.sort()
u = (a[0]+a[1])*a[2]
v = a[0]*a[1]*a[2]
print(max(u,v))
