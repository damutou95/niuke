n = 8
x = []#单个解
X = []#所有解的集合

def conflict(k):
    global x
    for i in range(k):
        if x[i] == x[k] or abs(x[i]-x[k]) == abs(i-k):
            return True
    return False


def queens(k):
    global x,X,n
    #最后一个皇后就位
    if k >= n:
        X.append(x[:])############
    else:
        for i in range(n):
            x.append(i)
            if not conflict(k):
                queens(k+1)
            x.pop()
if __name__ == '__main__':
    queens(0)
    for i in X:
        print(i)
    print(len(X))

