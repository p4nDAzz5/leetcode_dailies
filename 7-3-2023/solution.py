class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while nums[int((left+right)/2)] != target:
            if right-left < 2:
                if nums[right] == target:
                    return right
                elif nums[left] == target:
                    return left
                else:
                    return -1
            if nums[int((left+right)/2)] < target:
                left = int((left+right)/2)+1
            if nums[int((left+right)/2)] > target:
                right = int((left+right)/2)-1
        return int((left+right)/2)