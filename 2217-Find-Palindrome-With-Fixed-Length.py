class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        record={}
        if intLength==1:
            total=9
            record={i:i for i in range(10)}
        elif intLength==2:
            total=9
            record={i:i*11 for i in range(10)}
        else:
            total=(intLength+1)//2
            digits=1
            for i in range(total-1):
                digits*=10
            total=digits*9
        start=intLength%2
        ret=[-1]*len(queries)
        def calc(x):
            left=digits
            acc=1
            while left>0:
                if left!=digits:
                    acc*=10
                if x>=left:
                    acc+=x//left
                x=x%left
                left=left//10
            acc=str(acc)
            acc=acc+acc[::-1][start:]
            return int(acc)
        for i in range(len(queries)):
            cur=queries[i]
            if cur<=total:
                if cur not in record:
                    record[cur]=calc(cur-1)
                ret[i]=record[cur]
        return ret
