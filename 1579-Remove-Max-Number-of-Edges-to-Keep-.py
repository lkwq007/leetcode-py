class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        both_lst=[-1]*(n+1)
        def find(x,lst):
            tmp=x
            while lst[x]>=0:
                x=lst[x]
            while lst[tmp]>=0:
                next=lst[tmp]
                lst[tmp]=x
                tmp=next
            return x
        def union(u,v,lst):
            ui=find(u,lst)
            vi=find(v,lst)
            if ui!=vi:
                if ui>vi:
                    ui,vi=vi,ui
                lst[ui]+=lst[vi]
                lst[vi]=ui
            else:
                return True
            return False
        alice=[]
        bob=[]
        ret=0
        for t,u,v in edges:
            if t==1:
                alice.append((u,v))
            elif t==2:
                bob.append((u,v))
            else:
                if union(u,v,both_lst):
                    ret+=1
        alice_lst=both_lst[:]
        bob_lst=both_lst[:]
        for u,v in alice:
            if union(u,v,alice_lst):
                ret+=1
        for u,v in bob:
            if union(u,v,bob_lst):
                ret+=1
        alice_cnt=0
        bob_cnt=0
        for i in range(1,n+1):
            if alice_lst[i]<0:
                alice_cnt+=1
            if bob_lst[i]<0:
                bob_cnt+=1
        if alice_cnt==1 and bob_cnt==1:
            return ret
        else:
            return -1
                
                