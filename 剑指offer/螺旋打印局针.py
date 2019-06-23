# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        a = []
        while matrix != []:
            a += matrix.pop(0)
            matrix = self.turn(matrix)
        return a
    def turn(self,a):
        if a == []:
            return []
        b = []
        for i in range(len(a[0])):
            b.append([j.pop() for j in a])
        return b
