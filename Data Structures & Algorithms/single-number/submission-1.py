class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        for i in nums:
            result=i^result
        return result
                


