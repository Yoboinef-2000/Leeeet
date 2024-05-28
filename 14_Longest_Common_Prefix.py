class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        i = 1
        
        while i < len(strs):
            currentString = strs[i]
            j = 0
            while j < len(prefix) and j < len(currentString) and prefix[j] == currentString[j]:
                j += 1
            
            prefix = prefix[:j]
            
            if not prefix:
                return ""
            
            i += 1
        
        return prefix