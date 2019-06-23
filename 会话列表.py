s = int(input())
for i in range(s):
    a = int(input())
    b = input()
    c = [int(i) for i in b.split()]
    d = []
    while c != []:
        e = str(c.pop())
        if e not in d:
            d.append(e)
    print(' '.join(d))
