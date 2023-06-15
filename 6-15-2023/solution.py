class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = {} # sorted : index
        count = 0
        lst = []
        for elem in strs:
            temp = "".join(sorted(elem))
            if temp in hmap:
                lst[hmap[temp]].append(elem)
            else:
                hmap.update({temp:count})
                lst.append([elem])
                count += 1
        return lst
        
