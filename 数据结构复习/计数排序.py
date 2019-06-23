def sort(a):
    n = len(a)
    b = [None] * n
    for i in range(n):
        p = 0
        q = 0
        for j in range(n):
            if a[j] < a[i]:
                p += 1
            elif a[j] == a[i]:
                q += 1
        for k in range(p, p + q):
            b[k] = a[i]
    print(b)
if __name__ == "__main__":
    print(sort([1,3,5,5,5,8,4.5,]))
