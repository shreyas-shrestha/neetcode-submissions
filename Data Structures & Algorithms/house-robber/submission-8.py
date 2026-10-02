class Solution:
    def rob(self, nums: List[int]) -> int:
        L = [0] * len(nums)
        L[0] = nums[0]
        if len(nums) < 2:
            return L[0]
        L[1] = nums[1]
        if len(nums) < 3:
            return max(L[0], L[1])
        L[2] = max(nums[2] + nums[0], nums[1])
        for i in range(3, len(nums)):
            L[i] = max(L[i-2] + nums[i], L[i-1], L[i-3] + nums[i])
        return max(L[len(nums)-1], L[len(nums)-2])

        