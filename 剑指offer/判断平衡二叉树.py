# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    res = True
    def IsBalanced_Solution(self, pRoot):
        # write code here
        #如果规定空树为平衡二叉树那么需要下面这两行，如果没这规定那就删掉这两行
        if pRoot == None:
            return True
        self.deep(pRoot)
        return self.res
    def deep(self,root):
        if root == None:
            return 0
        left = 1 + self.deep(root.left)
        right = 1 + self.deep(root.right)
        if abs(left - right) > 1:
            self.res = False
        return max(left,right)
