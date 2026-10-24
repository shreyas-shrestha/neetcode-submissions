class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        check = len(digits)-1
        while digits[check] == 9:
            digits[check] = 0
            check-=1
            if check < 0:
                digits.insert(0,1)
                return digits
        digits[check]+=1   
        return digits