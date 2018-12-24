# ===================================================================================
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
# ===================================================================================

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        tail = head
        pre = head
        cur = head

        # ===================================================================================
        # Move tail nth step forward
        # We can do this beacause assumption is n is always valid
        # ===================================================================================
        while n>1:
            tail = tail.next
            n = n -1

        # ===================================================================================
        # Move tail to the end of the list
        # ===================================================================================
        while tail.next != None:
            tail = tail.next
            pre = cur
            cur = pre.next

        # ===================================================================================
        # Special case when we found the node need break is head node
        # ===================================================================================
        if cur == head:
            if head.next == None:
                return []
            else:
                head = head.next

        # ===================================================================================
        # Re-connect the pre and cur node
        # ===================================================================================
        pre.next = cur.next
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

model = Solution()
new_head = model.removeNthFromEnd(head = node1,n = 3)
print(new_head.val)
print(new_head.next.val)