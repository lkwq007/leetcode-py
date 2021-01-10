class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        # binary indexed tree
        term=10**9+7
        ret=0
        lst=list(sorted(instructions))
        prefix=[0]*(len(lst)+1)
        record={}
        for i,item in enumerate(lst,0):
            if item in record:
                record[item][1]=i
            else:
                record[item]=[i,i,i]
        def add(idx,val):
            idx+=1
            while idx<=len(lst):
                prefix[idx]+=val
                idx+=idx&(-idx)
        def calc(idx):
            idx+=1
            ret=0
            while idx>0:
                ret+=prefix[idx]
                idx-=idx&(-idx)
            return ret
        ret=0
        total=0
        for item in instructions:
            leftmost=record[item][0]
            if leftmost==0:
                ret+=0
                total+=1
                add(record[item][2],1)
                record[item][2]+=1
                continue
            else:
                leftmost-=1
            left=calc(leftmost)
            rightmost=record[item][1]
            right=calc(rightmost)
            ret+=min(left,total-right)
            ret%=term
            total+=1
            add(record[item][2],1)
            record[item][2]+=1
        return ret


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        # TLE
        term=10**9+7
        ret=0
        lst=[]
        record={}
        def search(val):
            l=0
            r=len(lst)
            while l<r:
                mid=l+(r-l)//2
                if lst[mid]>=val:
                    r=mid
                else:
                    l=mid+1
            return l
        lst.append(instructions[0])
        for item in instructions[1:]:
            if item in record:
                left,right=record[item]
            left=search(item)
            right=search(item+1)
            idx=left
            if len(lst)-right<left:
                idx=right
            # print(item,left,right,lst)
            ret+=min(left,len(lst)-right)
            lst.insert(idx,item)
            ret%=term
        return ret

class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.val=x
        self.cnt=1
        self.left_cnt=0

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        # TLE
        term=10**9+7
        ret=0
        root=Node(instructions[0])
        self.total=1
        def insert(node,val,acc):
            if val==node.val:
                node.cnt+=1
                left=node.left_cnt
                left+=acc
                return min(left,self.total-node.cnt-left)
            elif val<node.val:
                node.left_cnt+=1
                if node.left is None:
                    node.left=Node(val)
                    node.left.cnt=0
                return insert(node.left,val,acc)
            else:
                acc+=node.left_cnt+node.cnt
                if node.right is None:
                    node.right=Node(val)
                    node.right.cnt=0
                return insert(node.right,val,acc)
        for item in instructions[1:]:
            self.total+=1
            ret+=insert(root,item,0)
            ret%=term
        return ret
