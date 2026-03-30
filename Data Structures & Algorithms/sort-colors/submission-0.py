class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]<nums[j]:
                    c=nums[j]
                    nums[j]=nums[i]
                    nums[i]=c
        
        