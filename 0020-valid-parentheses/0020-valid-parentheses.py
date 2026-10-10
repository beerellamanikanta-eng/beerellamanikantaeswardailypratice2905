class Solution(object):
    def isValid(self, s):
        stack =[]
        for ch in s:
            if ch =="(":
                stack.append(")")
            elif ch =="{":
                stack.append("}")
            elif ch =="[":
                stack.append("]")
            else:
                if not stack or ch !=stack[-1]:
                    return False
                stack.pop()
        if stack :
            return False
        else:
            return True

        