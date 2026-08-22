class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        itemSort = [[] for x in range(len(nums) + 1)]
        toReturn = list()
        for i in nums:
            myDict[i] = myDict.get(i, 0) + 1
        for j in myDict:
            itemSort[myDict[j]].append(j)
        for l in reversed(itemSort):
                for i in l:
                    if k == 0:
                        return toReturn
                    else:
                        toReturn.append(i)
                        k = k - 1
        return toReturn

            
        
        

        