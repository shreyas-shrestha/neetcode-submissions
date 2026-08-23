class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left].isalnum() == False:
                left = left + 1
                continue
            elif s[right].isalnum() == False:
                right = right - 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            else:
                left = left + 1
                right = right - 1
        return True
        