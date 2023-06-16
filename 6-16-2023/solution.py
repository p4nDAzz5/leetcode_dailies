class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap.update({nums[i]:hmap[nums[i]]+1})
            else:
                hmap.update({nums[i]:1})

        returnList = []
        for i in range(k):
            highest = max(hmap, key=hmap.get)
            returnList.append(highest)
            del hmap[highest]

        return returnList
        