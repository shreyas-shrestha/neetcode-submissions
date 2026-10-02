class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recurse(nums, target, 0, len(nums)-1)
    
    def recurse(self, nums: List[int], target: int, left: int, right: int) -> int:
        if right < left: 
            return -1
        where_at = int((left + right) / 2)
        value = nums[where_at]
        if value > target:
            return self.recurse(nums, target, left, where_at - 1)
        elif value < target:
            return self.recurse(nums, target, where_at + 1, right)
        else:
            return where_at