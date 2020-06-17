class TreeNode:
    def __init__(self):
        self.endpoint=False
        self.children={}

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root=TreeNode()
        def insert(dirs):
            pwd=root
            for item in dirs:
                if pwd.endpoint:
                    break
                if item in pwd.children:
                    pwd=pwd.children[item]
                else:
                    tmp=TreeNode()
                    pwd.children[item]=tmp
                    pwd=tmp
            pwd.endpoint=True
        for item in folder:
            dirs=item.split("/")[1:]
            insert(dirs)
        ret=[]
        def dfs(node,path):
            if node.endpoint:
                ret.append(path)
                return
            for item in node.children:
                dfs(node.children[item],path+"/"+item)
        dfs(root,"")
        return ret
        