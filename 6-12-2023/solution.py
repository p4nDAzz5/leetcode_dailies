class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newSet = set()
        for num in nums:
            if num in newSet:
                return True
            newSet.add(num)
        return False