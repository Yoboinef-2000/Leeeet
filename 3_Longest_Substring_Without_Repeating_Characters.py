class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # i = 0
        # newS = []
        # mainSubString = []
        # for z in s:
        #     newS.append(z)
        
        maximumLength = 0
        start = 0
        characterIndices = {}
        
        for theEnd in range(len(s)):
            if s[theEnd] in characterIndices:
                start = max(start, characterIndices[s[theEnd]] + 1)
            
            characterIndices[s[theEnd]] = theEnd
            
            maximumLength = max(maximumLength, theEnd - start + 1)
        
        return maximumLength
