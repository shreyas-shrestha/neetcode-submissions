class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        toReturn = []
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in myDict:
                toReturn.append(myDict[remain])
                toReturn.append(i)
                return toReturn
            else:
                myDict[nums[i]]=i
        return toReturn


        