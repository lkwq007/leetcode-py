class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        # not unique
        B_map=[(val,idx) for idx,val in enumerate(B,0)]
        B_map.sort(key=lambda x:-x[0])
        A.sort(key=lambda x:-x)
        ret=[0]*len(A)
        head=0
        tail=len(A)-1
        b_head=0
        while head<=tail:
            val=B_map[b_head][0]
            idx=B_map[b_head][1]
            if A[head]>val:
                ret[idx]=A[head]
                head+=1
            else:
                ret[idx]=A[tail]
                tail-=1
            b_head+=1
        return ret
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        # not unique
        mapping={}
        for idx,item in enumerate(B,0):
            if item not in mapping:
                mapping[item]=[]
            mapping[item].append(idx)
        keys=list(mapping.keys())
        keys.sort(key=lambda x:-x)
        A.sort(key=lambda x:-x)
        ret=[0]*len(A)
        head=0
        tail=len(A)-1
        k_head=0
        while head<=tail:
            if A[head]>keys[k_head]:
                key=keys[k_head]
                idx=mapping[key]
                ret[idx[-1]]=A[head]
                head+=1
                idx.pop()
                if len(idx)<1:
                    k_head+=1
            else:
                key=keys[k_head]
                idx=mapping[key]
                ret[idx[-1]]=A[tail]
                tail-=1
                idx.pop()
                if len(idx)<1:
                    k_head+=1
        return ret