class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list.sort(nums)
        lcs = 1
        clcs = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            print(nums[i])
            if nums[i] == (nums[i-1] +1):
                clcs+=1
            elif nums[i] == nums[i-1]:
                continue
            else:
                if clcs > lcs:
                    lcs = clcs
                clcs = 1
        if clcs > lcs:
            lcs = clcs
        return lcs
            
        