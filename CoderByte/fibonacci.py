# Write a func fib(n) that takes in a number as an argument.
# The function should return the n-th number of the fibonacci sequence

class Solution(object):
    def fib(self, n):
        if n == 0 or n == 1:
            return n

        return self.fib(n-1) + self.fib(n-2)

    def fibWithMemo(self, n, memo={}):
        if n in memo: return memo[n]

        if n == 0 or n == 1: return n 
        
        memo[n] = self.fibWithMemo(n-1, memo) + self.fibWithMemo(n-2, memo)
        return memo[n]


obj = Solution()

num = 40 # 
# 0 1 1 2 3 5

result = obj.fibWithMemo(num)

print(result)