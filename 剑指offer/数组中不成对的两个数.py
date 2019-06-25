# -*- coding:utf-8 -*-
#这是常规方法
# class Solution:
#     # 返回[a,b] 其中ab是出现一次的两个数字
#     def FindNumsAppearOnce(self, array):
#         # write code here
#         temp = {}
#         for i in array:
#             if i not in temp.keys():
#                 temp[i] = i
#             else:
#                 del temp[i]
#         return temp.values()

#考察按位异或
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return []
        tmp = 0
        for i in array:
            tmp ^= i
        index = 0
        while (tmp & 1) == 0:
            tmp >>= 1
            index += 1
        a = b = 0
        for i in array:
            t = i
            t = t >> index
            if t&1:
                a ^= i
            else:
                b ^= i
        return [a,b]
