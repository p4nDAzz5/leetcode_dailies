class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        returnList = []
        for i in range(len(temperatures)):
            count = 0
            while i+count < len(temperatures) and temperatures[i] >= temperatures[i+count]:
                count+=1
            if i+count == len(temperatures):
                count = 0
            returnList.append(count)

        return(returnList)