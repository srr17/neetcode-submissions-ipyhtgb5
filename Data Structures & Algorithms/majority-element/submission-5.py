class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = 0
            c = nums[i]
            
            for j in range(len(nums)):
                if c == nums[j]:
                    n += 1
            
            if n > len(nums) // 2:
                return c
                