from linked_list.linked_list import ListNode



# 21. Merge Two Sorted Lists
def mergeTwoLists(list1, list2):
    # 處理list為空時的edge case
    if not list1:
        return list2
    if not list2:
        return list1
    
    # 創建linked list的頭
    if list1.val < list2.val:
        head = ListNode(list1.val)
        list1 = list1.next
    else:
        head = ListNode(list2.val)
        list2 = list2.next

    # 處理兩邊都還有資料的情況
    node = head
    while list1 and list2:
        if list1.val < list2.val:
            node.next = ListNode(list1.val)
            list1 = list1.next
        else:
            node.next = ListNode(list2.val)
            list2 = list2.next
        node = node.next

    # 有一邊沒資料了，直接串上另一邊資料
    if list1:
        node.next = list1
    else:
        node.next = list2

    return head


# 83. Remove Duplicates from Sorted List
def deleteDuplicates(head):
    node = head
    same_pointer = head

    # 處理edge case
    if not node or not node:
        return

    # 遍歷list每個node，下一個沒東西則跳出迴圈
    while node.next:
        front_value = node.val
        node = node.next

        # 如果數值不一樣，pointer往後指
        if front_value != node.val:
            print(front_value, node.val)
            same_pointer.next = node  # 往後指
            same_pointer = node  # 來到目前位置
    # 處理最後可能重複的部分
    same_pointer.next = None
    
    
# 141. Linked List Cycle
# my algorithm
def hasCycle(head):
    addr_dict = {}

    node = head
    while node:
        if node in addr_dict.keys():
            return True
        addr_dict[node] = node.val
        node = node.next
    return False


# 24. Swap Nodes in Pairs
def swapPairs(head):
    # 先處理edge case(0項或是1項)
    if not head or not head.next:
        return head

    # 2項以上
    # 處理首兩項
    node = head.next
    temp = head.next.next
    node.next = head
    head.next = temp
    head = node
    node = node.next

    while node.next and node.next.next:
        temp2 = node.next.next
        temp3 = node.next.next.next
        node.next.next.next = node.next
        node.next.next = temp3
        node.next = temp2

        node = node.next.next
    return head


        