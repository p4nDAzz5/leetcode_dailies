class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        counter = 1
        longest = 0
        if len(nums) <= 0:
            return 0
            
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i+1] == nums[i]+1:
                counter+=1
            else:
                if counter > longest:
                    longest = counter
                counter = 1
        if counter > longest:
            longest = counter
        return longest