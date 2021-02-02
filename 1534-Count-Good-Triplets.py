class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total=len(arr)
        ret=0
        for i in range(total):
            for j in range(i+1,total):
                for k in range(j+1,total):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[k]-arr[i])<=c:
                        ret+=1
        return ret

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total=len(arr)
        ret=0
        for i in range(total):
            for j in range(i+1,total):
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1,total):
                        if abs(arr[j]-arr[k])<=b and abs(arr[k]-arr[i])<=c:
                            ret+=1
        return ret