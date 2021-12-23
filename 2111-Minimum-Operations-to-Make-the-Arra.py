class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        # 1 <= arr.length <= 10**5
        # 1 <= arr[i], k <= arr.length
        ret=0
        for idx in range(k):
            lst=[]
            cnt=0
            while idx<len(arr):
                cnt+=1
                left=0
                right=len(lst)
                while left<right:
                    middle=left+(right-left)//2
                    if lst[middle]<(arr[idx],idx):
                        left=middle+1
                    else:
                        right=middle
                if right>=len(lst):
                    lst.append((arr[idx],idx))
                else:
                    lst[left]=(arr[idx],idx)
                idx+=k
            ret+=cnt-len(lst)
        return ret