# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1List = []
        l2List = []

        while l1 is not None:
            l1List.append(str(l1.val))
            l1 = l1.next
        while l2 is not None:
            l2List.append(str(l2.val))
            l2 = l2.next
        

        l1ReversedInt = int("".join(l1List[::-1]))
        l2ReversedInt = int("".join(l2List[::-1]))
        
        l1l2sum  = l1ReversedInt + l2ReversedInt
        l1l2sumStr = str(l1l2sum)
        l1l2reversedsumStr = l1l2sumStr [::-1]

        reversedNode = ListNode(int(l1l2reversedsumStr[0]))
        
        current = reversedNode
        for number in l1l2reversedsumStr[1:]:
            current.next = ListNode(int(number))
            current = current.next

        return (reversedNode)

