class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=list()
        for i in range(len(nums)):
            if nums[i] in c:
                return True
            c.append(nums[i])

        return False

        