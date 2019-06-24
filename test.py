class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        numbers = [str(i) for i in numbers]
        n = len(numbers)
        while n > 0:
            maxi = 0
            for i in range(n):
                if self.compareSort(numbers[i],numbers[maxi]):
                    maxi = i
            numbers[maxi],numbers[n-1] = numbers[n-1],numbers[maxi]
            n -= 1
        return ''.join(numbers)
    def compareSort(self,a,b):
        if a+b > b+a:
            return True
