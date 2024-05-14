class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        zigzagString = []
        for _ in range(numRows):
            zigzagString.append('')
    
        row, step = 0, 1

        for aLetter in s:
            zigzagString[row] += aLetter
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        return ''.join(zigzagString)
