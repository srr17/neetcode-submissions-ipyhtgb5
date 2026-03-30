class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        while len(nums1)>m:
            nums1.pop()
    
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        
        nums1.sort()
        