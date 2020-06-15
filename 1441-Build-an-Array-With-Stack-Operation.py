class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if n<1 or len(target)<1:
            return []
        stack=[]
        push="Push"
        pop="Pop"
        cur=1
        ret=[]
        for item in target:
            while cur<item:
                ret.append(push)
                ret.append(pop)
                cur+=1
            ret.append(push)
            cur+=1
        return ret                
