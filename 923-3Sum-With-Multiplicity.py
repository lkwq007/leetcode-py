class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        term=10**9+7
        lst=[0]*101
        ret=0
        for item in arr:
            lst[item]+=1
        for i in range(len(lst)):
            for j in range(i,len(lst)):
                tmp=i+j
                tmp=target-tmp
                if 0<=tmp<=100 and tmp>=j:
                    if i==j and j==tmp:
                        acc=(lst[i]-2)*(lst[i]-1)*lst[i]//6
                    elif i==j:
                        acc=(lst[i]-1)*lst[i]*lst[tmp]//2
                    elif j==tmp:
                        acc=lst[i]*lst[j]*(lst[j]-1)//2
                    else:
                        acc=lst[i]*lst[j]*lst[tmp]
                    ret+=acc
                    ret%=term
        return ret

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        term=10**9+7
        lst=[0]*101
        ret=0
        for item in arr:
            lst[item]+=1
        for i in range(len(arr)):
            lst[arr[i]]-=1
            new_lst=lst[:]
            for j in range(i+1,len(arr)):
                new_lst[arr[j]]-=1
                tmp=arr[i]+arr[j]
                tmp=target-tmp
                if 0<=tmp<=100:
                    ret+=new_lst[tmp]
                    ret%=term
            # for j in range(i+1,len(arr)):
            #     lst[arr[j]]+=1
        return ret
