from collections import deque
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # deque
        queue=deque([],maxlen=K)
        ret=K
        acc=0
        for i in range(len(A)):
            if A[i]==1:
                acc+=1
            else:
                head=queue[0] if queue else i
                if len(queue)==K:
                    acc=i-head
                else:
                    acc+=1
                queue.append(i)
            ret=max(ret,acc)
        return ret