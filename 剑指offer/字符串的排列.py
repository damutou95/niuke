# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        ss = list(ss)
        p = 0
        q = len(ss)
        # write code here
        d = []
        def permutation(ss,p,q):
            if p == q-1:
                if ''.join(ss) not in d:
                    d.append(''.join(ss))
            for i in range(p,q):
                ss[p], ss[i] = ss[i], ss[p]
                permutation(ss,p+1,q)
                ss[p], ss[i] = ss[i], ss[p]
        permutation(ss, p, q)
        d.sort()
        return d
