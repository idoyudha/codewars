# Write a function `canSum(targetSum, numbers)` that takes in a 
# targetSum and an array of numbers as arguments

# The function should return a boolean indicating whether or not it
# is possible to generate the targetSum using numbers from the array

class Solution(object):
    def canSum(self, targetSum, numbers):
        if targetSum == 0: return True
        if targetSum < 0: return False

        for num in numbers:
            remainder = targetSum - num
            if self.canSum(remainder, numbers) == True:
                return True

        # after try all possibilities in loop
        return False

    def canSumWithMemo(self, targetSum, numbers, memo={}):
        if targetSum in memo: return memo[targetSum]
        if targetSum == 0: return True
        if targetSum < 0: return False

        for num in numbers:
            remainder = targetSum - num
            if self.canSumWithMemo(remainder, numbers, memo) == True:
                memo[remainder] = True
                return True

        # after try all possibilities in loop
        memo[targetSum] = False
        return False


obj = Solution()

target = 300
numbers = [2,10]

result = obj.canSumWithMemo(target, numbers)

print(result)