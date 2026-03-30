class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        xors = [0]  
        
        for num in nums:
            new_xors = []
            for x in xors:
                new_xors.append(x ^ num)  
            xors += new_xors
        
        return sum(xors)