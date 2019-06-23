s = int(input())
for i in range(s):
    a = input().split()
    b = int(a[0])
    e = int(a[1])
    c = []
    for i in range(b):
        d = input()
        c.append(d)
    f = input()
    lengthWord = len(f)
    count = 0
    for i in range(b):
        for j in range(e):
            if j+lengthWord <= e:
                if  ''.join(c[i][j:j+lengthWord]) == f:
                    count += 1
            if i+lengthWord <= b:
                if  ''.join([c[i+m][j] for m in range(lengthWord)]) == f:
                    count += 1
            if i+lengthWord <= b and j+lengthWord <= e:
                if ''.join([c[i+m][j+m] for m in range(lengthWord)]) == f:
                    count += 1
    print(count)














