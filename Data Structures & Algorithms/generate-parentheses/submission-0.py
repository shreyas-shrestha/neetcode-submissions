class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset=""
        to_return = []
        self.backtrack(0, 0, 0, n, subset, to_return)
        return to_return
        
    def backtrack(self, index, opens, closes, n, subset, to_return):
        if index == ((2 * n)):
            to_return.append(subset)
            return
        if opens < n:
            self.backtrack(index+1, opens+1, closes, n, subset+"(", to_return)
        if closes < n and closes < opens:
            self.backtrack(index+1, opens, closes+1, n, subset+")", to_return)

        
        