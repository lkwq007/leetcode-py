# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def middle_split(ptr):
            slow=ptr
            fast=ptr
            prev=None
            while slow and fast:
                if fast.next:
                    fast=fast.next.next
                else:
                    break
                prev=slow
                slow=slow.next
            if prev:
                prev.next=None
            return slow
        def build_tree(ptr):
            if ptr is None:
                return None
            if ptr.next is None:
                return TreeNode(ptr.val)
            middle=middle_split(ptr)
            node=TreeNode(middle.val)
            node.left=build_tree(ptr)
            node.right=build_tree(middle.next)
            return node
        return build_tree(head)
        
def linked_list(lst):
    dummy_head=ListNode(0)
    prev=dummy_head
    for item in lst:
        node=ListNode(item)
        prev.next=node
        prev=node
    return dummy_head.next

x=Solution()
x.sortedListToBST(linked_list([-10,-3,0,5,9]))