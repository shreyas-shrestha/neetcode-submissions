class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalSum = 1
        numZeros = 0
        to_return = [0] * len(nums)
        for i in nums:
            if i != 0:
                totalSum*=i
            else:
                numZeros+=1
        for i in range(len(nums)):
            if numZeros == 1:
                if nums[i] == 0:
                    to_return[i] = totalSum
                else:
                    to_return[i] = 0
            elif numZeros > 1:
                to_return[i] = 0
            else:
                to_return[i] = int(totalSum / nums[i])
        return to_return
        