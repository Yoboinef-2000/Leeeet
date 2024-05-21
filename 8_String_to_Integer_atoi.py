class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        theImprovedS = []
        signEncountered = False

        for character in s:
            if character != " ":

                if character == "-" and not theImprovedS:
                    theImprovedS.append("-")
                    signEncountered = True

                elif character == "+" and not theImprovedS:
                    signEncountered = True
                
                elif signEncountered is True and (character == "-" or character == "+"):
                    return 0

                elif character.isdigit():
                    theImprovedS.append(character)

                else:
                    break

            elif signEncountered is True:
                theImprovedS = []
                break
            elif theImprovedS:
                break


        if not theImprovedS:
            return 0
        if theImprovedS[0] == "-" and len(theImprovedS) == 1:
            return 0
        if theImprovedS[0] == "-" and s[0] == "+":
            return 0

        theImprovedSint = int(''.join(theImprovedS))
        if theImprovedSint < -2 ** 31:
            return (-2 ** 31)
        if theImprovedSint > ((2 ** 31) -1):
            return (2 ** 31) -1
        return theImprovedSint

