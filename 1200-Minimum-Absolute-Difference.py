class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ret=[1]
        # len(arr)>=2
        diff=arr[1]-arr[0]
        for i in range(2,len(arr)):
            cur=arr[i]-arr[i-1]
            if cur<diff:
                ret=[i]
                diff=cur
            elif cur==diff:
                ret.append(i)
        return list(map(lambda idx:[arr[idx-1],arr[idx]],ret))