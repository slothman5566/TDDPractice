class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not(nums):
            return []
        return (list(set(range(1,max(max(nums),len(nums))+1))-set(nums)))
        
        