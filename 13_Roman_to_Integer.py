class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        theActualNumber = 0
        i = 0

        while (i < len(s) - 1):
            if s[i] == "I" and s[i + 1] == "V":
                theActualNumber += 4
                i += 1
            elif s[i] == "I" and s[i + 1] == "X":
                theActualNumber += 9
                i += 1
            elif s[i] == "X" and s[i + 1] == "L":
                theActualNumber += 40
                i += 1
            elif s[i] == "X" and s[i + 1] == "C":
                theActualNumber += 90
                i += 1
            elif s[i] == "C" and s[i + 1] == "D":
                theActualNumber += 400
                i += 1
            elif s[i] == "C" and s[i + 1] == "M":
                theActualNumber += 900
                i += 1
            else:
                theActualNumber += romanDict[s[i]]
            i += 1
            
        if i == len(s) - 1:
            theActualNumber += romanDict[s[i]]
        
        return theActualNumber
