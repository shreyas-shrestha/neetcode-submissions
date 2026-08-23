class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mostRecent = temperatures[0]
        myStack = []
        toReturn = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if temperatures[i] > mostRecent:
                index, currVal = myStack[-1]
                while len(myStack) > 0 and currVal < temperatures[i]:
                        myStack.pop()
                        toReturn[index] = i - index
                        if len(myStack) > 0:
                            index, currVal = myStack[-1]
            myStack.append((i, temperatures[i]))
            mostRecent = temperatures[i]
        return toReturn




            




        