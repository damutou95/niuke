# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if k not in data:
            return 0
        start = data.index(k)
        for i in range(start,len(data)):
            if i == len(data) - 1:
                return len(data) - start
            if data[i] != k:
                return i - start
