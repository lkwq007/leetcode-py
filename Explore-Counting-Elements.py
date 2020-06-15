class Solution:
    def countElements(self, arr: List[int]) -> int:
        record={}
        for item in arr:
            if item in record:
                record[item]+=1
            else:
                record[item]=1
        acc=0
        for key in record:
            tmp=key+1
            if tmp in record:
                acc+=record[key]
        return acc

class Solution:
    def countElements(self, arr: List[int]) -> int:
        if len(arr)<2:
            return 0
        arr.sort()
        cur=arr[0]
        cnt=1
        acc=0
        idx=1
        total=len(arr)
        while idx<total:
            if arr[idx]==cur:
                cnt+=1
            else:
                if arr[idx]==cur+1:
                    acc+=cnt
                cnt=1
                cur=arr[idx]
            idx+=1
        return acc