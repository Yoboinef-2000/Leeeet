class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        intStr = str(x)
        [l, r] = [0, len(intStr) - 1]
        while (l <= r):
            if (l == r):
                if intStr[l] == intStr[r]:
                    return True
    
            if intStr[l] != intStr[r]:
                return False

            l += 1
            r = r - 1

        return True
