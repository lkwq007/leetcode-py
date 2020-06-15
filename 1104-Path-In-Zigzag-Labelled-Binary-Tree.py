class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # complete binary tree
        if label==1:
            return [1]
        num=label
        depth=1
        while num>1:
            num=num>>1
            depth+=1
        def correct(x,depth):
            if depth%2==1:
                return x
            base=2**(depth-1)
            return base-(x-base)+base-1
        ret=[]
        pos=correct(label,depth)
        while pos>0:
            tmp=correct(pos,depth)
            ret.append(tmp)
            depth-=1
            pos=pos>>1
        return ret[::-1]