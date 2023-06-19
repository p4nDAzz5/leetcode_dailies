class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        response = ""
        for i in range(len(strs)):
            if i == len(strs) - 1:
                response = response + strs[i]
            else:
                response = response + strs[i] + ":;"
        return response

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        return str.split(":;")
