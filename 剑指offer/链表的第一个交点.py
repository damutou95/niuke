# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        s1 = []
        s2 = []
        res = []
        if not pHead1 or not pHead2:
            return None
        while pHead1 != None:
            s1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2 != None:
            s2.append(pHead2)
            pHead2 = pHead2.next
        while s1 and s2:
            n1 = s1.pop()
            n2 = s2.pop()
            if n1 == n2:
                res.append(n1)
            else:
                break
        if res:
            return res.pop()
