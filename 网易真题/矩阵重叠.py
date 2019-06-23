n = int(input())
x1 = [int(i) for i in input().split()]
y1 = [int(i) for i in input().split()]
x2 = [int(i) for i in input().split()]
y2 = [int(i) for i in input().split()]

result = 0;
for x in x1 + x2:
    for y in y1 + y2:
        count = 0
        for i in range(n):
            if x >= x1[i] and y >= y1[i] and x < x2[i] and y < y2[i]:
                count += 1
        result = max(result, count)
print(result)
