class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,1000):
            if i in nums:
                continue
            else:
                return(i)