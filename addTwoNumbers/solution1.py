# Definition for singly-linked list.

# ===================================================================================
# Accepted, even though there are faster solutions,
# but this solution take consideration for large numbers
# ===================================================================================

import copy
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        advance_num = 0
        header = ListNode(-1)
        point = header
        while l1.next is not None or l2.next is not None:
            point,advance_num = self.sum_two_nodes(l1,l2,advance_num,point)
            l1,l2 = self.advance(l1,l2)

        point, advance_num = self.sum_two_nodes(l1, l2, advance_num, point)
        if advance_num == 1: point.next = ListNode(1)

        return header.next

    def sum_two_nodes(self,l1,l2,advance_num,point):
        temp_sum = l1.val + l2.val + advance_num
        if temp_sum >= 10:
            temp_sum = temp_sum - 10
            advance_num = 1
        else:
            advance_num = 0

        point.next = ListNode(temp_sum)
        point = point.next
        return point,advance_num

    def advance(self,l1,l2):
        if l1.next is None:
            l2 = l2.next
            l1 = ListNode(0)
        elif l2.next is None:
            l1 = l1.next
            l2 = ListNode(0)
        else:
            l1 = l1.next
            l2 = l2.next
        return l1,l2

num1 = [2,4,9,3,2,2,3,2,1,3,2,4,6,7,8,9,2,3,4,5,3,2,1,2,4,5,6,7,8,9,9,2]
num2 = [0,6,4,0,0,0,0,0,0,0,0,0,0,0,0,3]

def generate_list(nums):
    nodes ={}
    for i in range(len(nums)):
        nodes[i] = ListNode(nums[i])

    for j in range(len(nums)-1):
        nodes[j].next = nodes[j+1]
    return nodes[0]

def print_nodes(head):
    p = copy.deepcopy(head)
    while p.next is not None:
        print(p.val)
        p = p.next
    print(p.val)


head1 = generate_list(num1)
head2 = generate_list(num2)
obj = Solution()
k1 = obj.addTwoNumbers(head1,head2)
print_nodes(k1)
