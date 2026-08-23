class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        theSum = numbers[left] + numbers[right]
        while theSum != target:
            if theSum < target:
                left = left + 1
            elif theSum > target:
                right = right - 1
            theSum = numbers[left] + numbers[right]
        return [left + 1, right + 1]
            
        
        