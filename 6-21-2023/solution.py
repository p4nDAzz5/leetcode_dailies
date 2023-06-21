class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for i in range(len(s)):
            if s[i] in brackets.values() and stack != [] and brackets.keys()[brackets.values().index(s[i])] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        else:
            return False