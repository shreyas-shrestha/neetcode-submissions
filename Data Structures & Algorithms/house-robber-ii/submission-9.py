class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        backNums = list(reversed(nums))
        F = [0] * len(nums)
        L = [0] * len(nums)
        F[0] = nums[0]
        F[1] = max(nums[1], nums[0])
        L[0] = backNums[0]
        L[1] = max(backNums[1], backNums[0])
        if len(nums) == 2:
            return max(L[1], F[1])
        for i in range(2, len(nums)-1):
            if i > 2:
                F[i] = max(F[i-2] + nums[i], F[i-1], F[i-3] + nums[i])
            else: 
                F[i] = max(F[i-2] + nums[i], F[i-1])
        for j in range(2, len(nums)-1):
            if j > 2:
                L[j] = max(L[j-2] + backNums[j], L[j-1], L[j-3] + backNums[j])
            else: 
                L[j] = max(L[j-2] + backNums[j], L[j-1])
        return max(L[len(nums)-2], F[len(nums)-2])




        