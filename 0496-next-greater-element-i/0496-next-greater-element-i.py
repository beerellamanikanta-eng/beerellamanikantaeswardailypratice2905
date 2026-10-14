
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        k = {}

        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                k[nums2[i]] = stack[-1]
            else:
                k[nums2[i]] = -1
            stack.append(nums2[i])
        ans = []
        for num in nums1:
            ans.append(k[num])
        return ans
