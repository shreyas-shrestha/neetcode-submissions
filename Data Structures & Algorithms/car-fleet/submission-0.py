class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tempStack = []
        for i in range(len(position)):
            tempStack.append((position[i], speed[i]))
        myStack = sorted(tempStack)
        fleets = 1
        firstPos, firstSpeed = myStack.pop()
        currentFleet = (target - firstPos) / firstSpeed
        while len(myStack) > 0:
            currPos, currSpeed = myStack.pop()
            tempFleet = (target - currPos) / currSpeed
            if tempFleet > currentFleet:
                currentFleet = tempFleet
                fleets = fleets + 1
        return fleets
