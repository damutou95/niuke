def compareSort(a,b):
    if a+b > b+a:
        return True

def partition(origin,p,q):
    tag = origin[p]
    l = p + 1
    r = q
    while True:
        while l <= r and compareSort(tag,origin[l]):
            l += 1
        while l <= r and compareSort(origin[r],tag):
            r -= 1
        if r < l:
            break
        origin[l], origin[r] = origin[r], origin[l]
    origin[r], origin[p] = origin[p], origin[r]
    return r

def fastSortHelper(origin,p,q):
    if p<q:
        mid = partition(origin,p,q)
        fastSortHelper(origin,p,mid-1)
        fastSortHelper(origin,mid+1,q)

def fastSort(origin):
    p = 0
    q = len(origin) - 1
    fastSortHelper(origin,p,q)


if __name__ == '__main__':
    a = [54,26,93,17,77,31,44,55,20]
    fastSort(a)
    print(a)


