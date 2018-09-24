# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
The following is a solution of Add two numbers problem which is described as:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class Solution:
    def listToInt(self, list, base=10):
        node = list
        i = 0
        place = 1
        while node is not None:
            i += (node.val*place)
            node = node.next
            place *= base
        return i
    
    def intToList(self, inputNum, base=10):
        head = ListNode(0)
        lastNode = head
        stringRep = str(inputNum)
        while stringRep != "":
            digit = stringRep[-1:]
            stringRep = stringRep[:-1]
            nextNode = ListNode(int(digit))
            lastNode.next = nextNode
            lastNode = nextNode
        return head.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        newint = self.listToInt(l1) + self.listToInt(l2)
        return self.intToList(newint)
