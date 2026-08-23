class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        toReturn = []
        myNums = sorted(nums)
        for i in range(len(myNums) - 2):
            left = i + 1
            right = len(myNums) - 1
            while left < right:
                currSum = myNums[i] + myNums[left] + myNums[right]
                if currSum > 0:
                    right = right - 1
                elif currSum < 0:
                    left = left + 1
                else:
                    arr = [myNums[i], myNums[left], myNums[right]]
                    if arr not in toReturn:
                        toReturn.append(arr)
                    left = left + 1
                    right = right - 1

        return toReturn






            
        