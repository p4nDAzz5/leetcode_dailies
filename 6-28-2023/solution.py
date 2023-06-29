class Solution(object):
    def isPalindrome(self, s):
        import re
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True