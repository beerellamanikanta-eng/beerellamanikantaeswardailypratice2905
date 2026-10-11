class Solution(object):
    def reverseVowels(self, s):
       k ="aeiouAEIOU"
       s =list(s)
       left =0
       right =len(s)-1
       while left < right:
        if s[left] not in k:
            left+=1
        elif s[right] not in k:
            right-=1
        else:
            s[left],s[right] =s[right],s[left]
            left+=1
            right-=1
       return "".join(s)
    


        