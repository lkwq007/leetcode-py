"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        queue=[(root,0)]
        idx=0
        last=None
        cur=-1
        while idx<len(queue):
            node,depth=queue[idx]
            if cur!=depth:
                last=node
                cur=depth
            else:
                last.next=node
                last=node
            idx+=1
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        return root

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect_node(node,parent,left=True):
            if node is None:
                return
            if parent is None:
                node.next=None
                connect_node(node.right,node,False)
                connect_node(node.left,node)
            else:
                if left and parent.right:
                    node.next=parent.right
                else:
                    ptr=parent.next
                    while ptr:
                        if ptr.left:
                            ptr=ptr.left
                            break
                        if ptr.right:
                            ptr=ptr.right
                            break
                        ptr=ptr.next
                    node.next=ptr
                if node.right:
                    connect_node(node.right,node,False)
                if node.left:
                    connect_node(node.left,node)
        connect_node(root,None)
        return root

x=Solution()
tree=Node(0)
tree.left=Node(1)
tree.right=Node(2)
print(tree.next,tree.left.next,tree.right.next)

print(x.connect(tree))
print(tree.next,tree.left.next,tree.right.next)
