class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringMap = {}
        for i in s:
            if i in stringMap:
                stringMap[i] = stringMap[i] + 1
            else:
                stringMap[i] = 1
        for j in t:
            if j in stringMap:
                if stringMap[j] == 1:
                    del stringMap[j]
                else:
                    stringMap[j] = stringMap[j] - 1
            else:
                return False
        if len(stringMap) == 0:
            return True
        return False
            
        