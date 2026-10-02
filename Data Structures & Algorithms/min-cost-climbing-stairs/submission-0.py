class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        T = [0] * (len(cost))
        T[0] = cost[0]
        T[1] = cost[1]
        for i in range(2, len(cost)):
            T[i] = min(T[i-2], T[i-1]) + cost[i]
        return min(T[len(T)-1], T[len(T)-2])



            
        
        
        