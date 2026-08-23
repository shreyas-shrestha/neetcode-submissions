class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        toReturn = list()
        for i in strs:
            val = tuple(sorted(i)) 
            if val not in myDict:
                arr = list()
                arr.append(i)        
                myDict[val] = arr
            else:
                myDict[val].append(i)
        for i in myDict.values():
            toReturn.append(i)
        return toReturn