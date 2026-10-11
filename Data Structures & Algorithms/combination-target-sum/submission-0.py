class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        to_return = []
        subset = []
        self.dfs(nums, 0, 0, to_return, subset, target)
        return to_return

    def dfs(self, nums, value, index, to_return, subset, target):
        if value > target:
            return
        if value == target:
            to_return.append(subset.copy())
            return
        if index >= len(nums):
            return
        subset.append(nums[index])
        self.dfs(nums, value + nums[index], index, to_return, subset, target)
        subset.pop()
        self.dfs(nums, value, index+1, to_return, subset, target)

        



        