class Solution:
    def reinitializePermutation(self, n: int) -> int:
        lst=[(n//2+i//2) if i&1 else i//2 for i in range(n)]
        self.cnt=[]
        def dfs(x,acc):
            if lst[x]==x or lst[x]==-1:
                self.cnt.append(acc)
                return
            next=lst[x]
            lst[x]=-1
            dfs(next,acc+1)
        for i in range(n):
            if lst[i]>=0:
                dfs(i,0)
        lst=list(set([item for item in self.cnt if item>0]))
        if len(lst)<1:
            return 1
        init=lst[:]
        def check(arr):
            for i in range(len(arr)):
                if arr[i]!=arr[i-1]:
                    return True
            return False
        while check(lst):
            item=min(lst)
            for i in range(len(lst)):
                if item==lst[i]:
                    lst[i]+=init[i]
        return lst[0]