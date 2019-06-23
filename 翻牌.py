s = int(input())
for i in range(s):
    c = [int(i) for i in input().split()]
        if c[0] >1 and c[1]>1:
            print(c[0]*c[1]-c[0]*2-c[1]*2 + 4)
        elif c[0] == 1 and c[1] == 1:
            print(1)
        elif c[0] >1 and c[1] == 1:
            if c[0]%2 == 1:
                print(c[0] - 2)
        elif c[0] == 1 and c[1] >1:
            if c[1]%2 == 1:
                print(c[1] - 2)

