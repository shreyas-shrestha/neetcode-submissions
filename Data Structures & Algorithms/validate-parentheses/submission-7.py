class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {"(":")","{":"}", "[":"]"}
        myStack = []
        for i in s:
            if i in myDict:
                myStack.append(myDict[i])
            elif len(myStack) == 0:
                return False
            else:  
                curr = myStack.pop()
                if i != curr:
                    return False
        if len(myStack) == 0:
            return True
        return False
            
        