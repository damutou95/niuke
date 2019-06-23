# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here

        while sequence:
            a = sequence[-1]
            b = [i for i in sequence[:-1] if i < sequence[-1]]
            c = [i for i in sequence[:-1] if i > sequence[-1]]
            if b + c != sequence[:-1]:
                return False
            else:
                sequence.pop()
                self.VerifySquenceOfBST(b)
                self.VerifySquenceOfBST(c)
        return True

