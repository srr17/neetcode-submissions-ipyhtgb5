class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]<nums[j]:
                    c=nums[j]
                    nums[j]=nums[i]
                    nums[i]=c
        return nums