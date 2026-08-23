class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        firstVal = 0
        secondVal = 0
        mySet = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] in mySet:
                secondVal = int(numStack.pop())
                firstVal = int(numStack.pop())
                if tokens[i] == "+":
                    secondVal = int(firstVal + secondVal)
                if tokens[i] == "-":
                    secondVal = int(firstVal - secondVal)
                if tokens[i] == "*":
                    secondVal = int(firstVal * secondVal)
                if tokens[i] == "/":
                    secondVal = int(firstVal / secondVal)
                numStack.append(secondVal)          
            if tokens[i] not in mySet: 
                numStack.append(int(tokens[i]))
        return numStack.pop()

            


        