x = []
def permutation(origin,left,right):
    global x
    if left == right:
        x.append(origin[:])
    for i in range(left,right):
        origin[left],origin[i] = origin[i],origin[left]
        permutation(origin,left+1,right)
        origin[left], origin[i] = origin[i], origin[left]


permutation([1,2,3,4],0,4)
for i in x:
    print(i)


