# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        a = []
        for i in range(k):
            self.heapAll(tinput,len(tinput))
            tinput[0], tinput[-1] = tinput[-1], tinput[0]
            a.append(tinput.pop())
        return a
    def heapfy(self, tree, n, i):
        if i > n:
            return None
        minIndex = i
        c1 = 2*i + 1
        c2 = 2*i + 2
        if c1 < n and tree[minIndex] > tree[c1]:
            minIndex = c1
        if c2 < n and tree[minIndex] > tree[c2]:
            minIndex = c2
        if minIndex != i:
            tree[minIndex], tree[i] = tree[i], tree[minIndex]
            self.heapfy(tree, n, minIndex)
    def heapAll(self, tree, n):
        lastParent = (n - 1 - 1) / 2
        for j in range(lastParent, -1, -1):
            self.heapfy(tree, n, j)


