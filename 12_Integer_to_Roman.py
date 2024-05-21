class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        theRomanStr = []
        romanDict = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        

        values = sorted(romanDict.keys(), reverse=True)
        
        for value in values:
            while num >= value:
                theRomanStr.append(romanDict[value])
                num -= value

        return ''.join(theRomanStr)
