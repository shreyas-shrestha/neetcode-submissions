class Solution:

    def encode(self, strs: List[str]) -> str:
        toReturn = ""
        for i in strs:
            toReturn += str(len(i)) + "-"
            for chars in i:
                toReturn+=chars
        return toReturn


    def decode(self, s: str) -> List[str]:
        toReturn = list()
        readNum = True
        val = 0
        stringVal = ""
        currWord = ""
        for i, chars in enumerate(s):
            if readNum == True:
                if chars == "-":
                    val = int(stringVal)
                    stringVal = ""
                    readNum = False
                    if val == 0:
                        toReturn.append(currWord)
                        readNum = True
                else:
                    stringVal += chars
            else:
                val = val - 1
                if val > 0:
                    currWord+=chars
                else:
                    currWord+=chars
                    toReturn.append(currWord)
                    currWord = ""
                    readNum = True
        return toReturn

                

            
