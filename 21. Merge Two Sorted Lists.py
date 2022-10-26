# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
        

def initialize(array):
    if (len(array) == 0):
        return []
    head = ListNode(array[0])
    current = head

    for i in range(1, len(array)):
        newNode = ListNode(array[i])
        current.next = newNode
        current = current.next
    
    return head

def printLinkedList(head):
    current = head
    printStr = ""

    while (current):
        printStr += (str(current.val) + "->")
        current = current.next

    print(printStr)

list1 = [1,3,5]
list2 = [1,2,3]
linked1 = initialize(list1)
linked2 = initialize(list2)
printLinkedList(linked1)
printLinkedList(linked2)

s = Solution()
printLinkedList(s.mergeTwoLists(linked1, linked2))
