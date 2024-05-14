class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x <= -2 ** 31) or (x >= ((2 ** 31) - 1)):
            return 0
        
        intString = str(x)
        i = len(intString) - 1
        reversedIntString = []
        j = 0

        if intString[0] == "-":
                reversedIntString.append("-")
        while i >= 0:
            if intString[i] == "-":
                break
            reversedIntString.append(intString[i])
            i = i - 1
        reversedInt = ''.join(reversedIntString)

        if (int(reversedInt) <= -2 ** 31) or (int(reversedInt)>= ((2 ** 31) - 1)):
            return 0
        return (int(reversedInt))


        
