# may TLE/accept
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree=[(0,)*5]*(len(s)*4)
        lst=[-ord(item) for item in s]
        def combine(v,tl,tm,tr):
            left=tree[v*2]
            right=tree[v*2+1]
            lenl=tm-tl+1
            lenr=tr-tm
            val0=left[0] if left[0]>right[0] else right[0]
            val1=left[1]
            val3=left[3]
            val2=right[2]
            val4=right[4]
            if left[4]==right[3]:
                mid=left[2]+right[1]
                if mid>val0:
                    val0=mid
                if left[1]==lenl:
                    val1+=right[1]
                if right[2]==lenr:
                    val2+=left[2]
            tree[v]=(val0,val1,val2,val3,val4)
        def update(v,tl,tr,pos,val):
            if tl==tr:
                tree[v]=(1,1,1,val,val)
            else:
                tm=(tl+tr)//2
                if pos<=tm:
                    update(v*2,tl,tm,pos,val)
                else:
                    update(v*2+1,tm+1,tr,pos,val)
                combine(v,tl,tm,tr)
        def build(v,tl,tr):
            if tl==tr:
                tree[v]=(1,1,1,lst[tl],lst[tl])
            else:
                tm=(tl+tr)//2
                build(v*2,tl,tm)
                build(v*2+1,tm+1,tr)
                combine(v,tl,tm,tr)
        build(1,0,len(s)-1)
        ret=[0]*len(queryCharacters)
        for i,(qc,qi) in enumerate(zip(queryCharacters,queryIndices)):
            val=-ord(qc)
            if lst[qi]!=val:
                lst[qi]=val
                update(1,0,len(s)-1,qi,val)
            ret[i]=max(tree[1])
        return ret

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree=[[0]*5 for _ in range(len(s)*4)]
        lst=[-ord(item) for item in s]
        def combine(v,tl,tm,tr):
            left=tree[v*2]
            right=tree[v*2+1]
            lenl=tm-tl+1
            lenr=tr-tm
            tree[v][0]=left[0] if left[0]>right[0] else right[0]
            tree[v][1]=left[1]
            tree[v][3]=left[3]
            tree[v][2]=right[2]
            tree[v][4]=right[4]
            if left[4]==right[3]:
                mid=left[2]+right[1]
                if mid>tree[v][0]:
                    tree[v][0]=mid
                if left[1]==lenl:
                    tree[v][1]+=right[1]
                if right[2]==lenr:
                    tree[v][2]+=left[2]
        def update(v,tl,tr,pos,val):
            if tl==tr:
                tree[v][3]=val
                tree[v][4]=val
            else:
                tm=(tl+tr)//2
                if pos<=tm:
                    update(v*2,tl,tm,pos,val)
                else:
                    update(v*2+1,tm+1,tr,pos,val)
                combine(v,tl,tm,tr)
        def build(v,tl,tr):
            if tl==tr:
                tree[v][0]=1
                tree[v][1]=1
                tree[v][2]=1
                tree[v][3]=lst[tl]
                tree[v][4]=lst[tl]
            else:
                tm=(tl+tr)//2
                build(v*2,tl,tm)
                build(v*2+1,tm+1,tr)
                combine(v,tl,tm,tr)
        build(1,0,len(s)-1)
        ret=[0]*len(queryCharacters)
        for i,(qc,qi) in enumerate(zip(queryCharacters,queryIndices)):
            val=-ord(qc)
            if lst[qi]!=val:
                lst[qi]=val
                update(1,0,len(s)-1,qi,val)
            ret[i]=max(tree[1])
        return ret
        