
class Solution(object):
    def minSwaps(self, nums):
        def digitSum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        arr = sorted(nums, key=lambda x: (digitSum(x), x))
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i
        swaps = 0
        for i in range(len(nums)):
            if nums[i] != arr[i]:
                j = pos[arr[i]]
                pos[nums[i]] = j
                pos[arr[i]] = i
                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1
        return swaps
