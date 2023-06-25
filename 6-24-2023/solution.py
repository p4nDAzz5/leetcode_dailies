class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def recursePara(s, o, c, n, stack):
            if o == n and c == n:
                stack.append(s)
                return
            if o > c:
                recursePara(s + ")", o, c+1, n, stack)
            if o < n:
                recursePara(s + "(", o+1, c, n, stack)

        returnStack = []
        recursePara("", 0, 0, n, returnStack)

        return returnStack