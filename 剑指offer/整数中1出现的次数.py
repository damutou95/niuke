# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        i = 1
        count = 0
        while i <= n:
            count += n/(i*10)*i + (i if n%(i*10)> 2*i-1 else 0 if n%(i*10)<i else n%(i*10)-i+1)
            i *= 10
        return count
