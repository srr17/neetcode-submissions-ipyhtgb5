class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:  
        s1 = 0  
        s2 = 0 

        for i in cost:
            curr = i + min(s1, s2)
            s2 = s1
            s1 = curr

        return min(s1, s2)