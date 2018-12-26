import copy

# ===================================================================================
# Use Priority queue, actually it is slower than dict!
# ===================================================================================

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        for head in lists:
            while head is not None:
                q.put(head.val)
                head = head.next

        nodes = []
        while not q.empty():
            k = q.get()
            node = ListNode(k)
            if len(nodes) > 0: nodes[-1].next = node
            nodes.append(node)

        if len(nodes)>0 :return nodes[0]

num1 = [2,4,9]
num2 = [0,2,7,10]
num3 = [9]
num4 = [3,2]

def generate_list(nums):
    if len(nums) ==0: return None
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
head3 = generate_list(num3)
head4 = generate_list(num4)
obj = Solution()
k1 = obj.mergeKLists([head1,head2,head3])
print_nodes(k1)
