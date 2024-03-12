from linked_list.linked_list import *
from linked_list.operation import *



# LEECODE SOLUTION #
# 21. Merge Two Sorted Lists
'''
list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))


# index count of arrays
reslut = mergeTwoLists(list1, list2)
reslut.print_list()
'''

# 83. Remove Duplicates from Sorted List
'''
list1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, None))))))

deleteDuplicates(list1)
list1.print_list()
'''


# 141. Linked List Cycle
'''
tail = ListNode(4, None)
head = ListNode(3, ListNode(2, ListNode(0, tail)))
tail.next = head.next
print(hasCycle(head))
'''


# 24. Swap Nodes in Pairs
'''
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, None)))))))
list1 = swapPairs(list1)
list1.print_list()
'''

# 61. Rotate List
list1 = ListNode(1, None)
list1 = rotateRight(list1, 10)
list1.print_list()