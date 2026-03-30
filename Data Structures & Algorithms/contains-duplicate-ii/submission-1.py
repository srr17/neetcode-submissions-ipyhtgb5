class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l1=[]
        for i in range(len(nums)):
            if nums[i] in l1:
                return True
            l1.append(nums[i])
        
            if len(l1)>k:
                l1.remove(nums[i - k])

        return False
        