class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        for i in s:
            myDict[i] = myDict.get(i, 0) + 1
        for j in t:
            if j not in myDict:
                return False
            elif myDict[j] > 1:
                myDict[j] = myDict.get(j) - 1
            else:
                myDict.pop(j)
        if not myDict:
            return True
        return False
