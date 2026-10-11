class Solution(object):
    def validPalindrome(self, s):
        def p(left, right, s):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return p(left + 1, right, s) or p(left, right - 1, s)
        return True