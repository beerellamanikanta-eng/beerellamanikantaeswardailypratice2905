
class Solution(object):
    def maxAlternatingSum(self, nums):
        nums = [x * x for x in nums]
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            if i < n // 2:
                ans -= nums[i]
            else:
                ans += nums[i]
        return ans
