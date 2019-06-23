import copy
s = input()
a = input().split()
c = []
b = []
def reverse(b):
    f = []
    while b != []:
        f.append(b.pop())
    return f

while a != []:
    c.append(a.pop(0))
    # c = reverse(c)
    c = list(reversed(c))
print(' '.join(c))

