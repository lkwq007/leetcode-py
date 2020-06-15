# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = []
        cur = 0
        # level scan
        root_bak = root
        queue.append(root)
        ret = []
        while cur < len(queue):
            node = queue[cur]
            cur += 1
            if node is None:
                ret.append("n")
            else:
                ret.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return " ".join(ret)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split()
        idx = 0
        val = nodes[idx]
        idx += 1
        if val == "n":
            return None
        node = TreeNode(int(val))
        root = node
        queue = [node]
        cur = 0
        while cur < len(queue):
            node = queue[cur]
            cur += 1
            left = nodes[idx]
            right = nodes[idx + 1]
            idx += 2
            if left == "n":
                node.left = None
            else:
                tmp = TreeNode(int(left))
                node.left = tmp
                queue.append(tmp)
            if right == "n":
                node.right = None
            else:
                tmp = TreeNode(int(right))
                node.right = tmp
                queue.append(tmp)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
