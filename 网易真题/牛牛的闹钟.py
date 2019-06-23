n = int(input())
t = []
for i in range(n):
    t.append(list(map(int,input().split())))
dis = int(input())
course = list(map(int,input().split()))
t = sorted(t,key=lambda x:int(''.join(list(map(lambda j:(str(j)).zfill(2),x)))))
def biggerThan(A,B):
    if A[0] > B[0]:
        return True
    elif A[0] == B[0]:
        if A[1] > B[1]:
            return True
    else:
        return False

def add(A,d):
    C = A.copy()
    go = (C[1] + d)//60#python2中用一个斜杠
    rest = (C[1] + d)%60
    C[0] = C[0] + go
    C[1] = rest
    return C
if __name__ == "__main__":
    while t != []:
        s = t.pop()
        if not biggerThan(add(s,dis), course):
            print(' '.join(map(str,s)))
            break


