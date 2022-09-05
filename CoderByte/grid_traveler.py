# Say that you are a traveler on a 2D grid. 
# You begin in the top-left corner and your goal is to travel to the bottom-right corner
# You may only move down or right

# In how many ways can you travel to the goal on a grid with dimension m * n?

# Write a function `gridTraveler(m, n)` that calculate this.

class Solution(object):
    def gridTraveler(self, m, n):
        # every 1 in m or n, it just one way
        if m == 1 or n == 1: return 1 

        return self.gridTraveler(m-1, n) + self.gridTraveler(m, n-1)

    def gridTravelerMemo(self, m, n, memo={}):
        key = str(m) + ',' + str(n)
        if key in memo: return memo[key]

        if m == 1 or n == 1: return 1

        memo[key] = self.gridTravelerMemo(m-1, n, memo) + self.gridTravelerMemo(m, n-1, memo)

        return memo[key]


obj = Solution()

x = 40
y = 40

result = obj.gridTravelerMemo(x, y)

print(result)