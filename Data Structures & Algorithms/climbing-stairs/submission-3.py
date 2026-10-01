class Solution:
    def climbStairs(self, n: int) -> int:
        values = max(3, n+1)
        T = [0] * (values)
        T[1] = 1
        T[2] = 2
        for i in range(3, n+1):
            T[i] = T[i-1] + T[i-2]
        return T[n]

        
        