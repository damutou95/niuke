s = [int(i) for i in input().split()]
a = s[0] - s[1] if s[0] > s[1] else s[1]- s[0]
b = s[0] - s[2] if s[0] > s[2] else s[2]- s[0]
c = s[2] - s[1] if s[2] > s[1] else s[1]- s[2]
print(a + b + c - max(a,b,c))
