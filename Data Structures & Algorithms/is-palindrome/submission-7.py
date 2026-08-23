class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left].isalnum() == False:
                left+= 1
                continue
            if s[right].isalnum() == False:
                right = right - 1
                continue
            if s[left] != s[right]:
                return False
            else:
                left = left + 1
                right = right - 1
        return True
        