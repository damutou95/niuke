def merge(a,b):
    atag = 0
    btag = 0
    ctag = 0
    c = []
    if a != None and b != None:
        while atag < len(a) and btag < len(b):
            if a[atag] < b[btag]:
                c.insert(ctag,a[atag])
                atag += 1
                ctag += 1
            else:
                c.insert(ctag,b[btag])
                btag += 1
                ctag += 1
        if atag < len(a):
            c = c + a[atag:]
        if btag < len(b):
            c = c + b[btag:]
        return c
def mergeSort(origin):
    if len(origin) > 1:
        mid = len(origin)//2#python2用/
        a = mergeSort(origin[:mid])
        b = mergeSort(origin[mid:])
        return merge(a,b)
    else:
        return origin

if __name__ == "__main__":
    print(mergeSort([1,3,3.5,2,3,4,2,3,7.5,3.5,4.5]))
