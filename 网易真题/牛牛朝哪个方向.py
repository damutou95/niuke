n = int(input())
s = input()
tag = 0
d = {0:'N',1:'W',2:'S',3:'E'}
for i in s:
    if i == 'L':
        tag += 1
    if i == 'R':
        tag -= 1
    if tag < 0:
        tag = tag + 4
print(d[tag%4])
