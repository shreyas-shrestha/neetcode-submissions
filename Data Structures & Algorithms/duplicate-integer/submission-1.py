class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myHashSet = set()
        for x in range(len(nums)):
            if nums[x] in myHashSet:
                return True
            myHashSet.add(nums[x])
        return False

        