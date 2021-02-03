class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # binary search
        base=ord("a")
        def freq(x):
            lst=[0]*26
            ret=25
            for item in x:
                lst[ord(item)-base]+=1
            for i in range(26):
                if lst[i]>0:
                    return lst[i]
            return 0
        freq_lst=[freq(item) for item in words]
        freq_lst.sort()
        def search(target):
            left=0
            right=len(queries)-1
            while left<right:
                middle=left+(right-left)//2
                if freq_lst[middle]<=target:
                    left=middle+1
                else:
                    right=middle
            while left<len(freq_lst) and freq_lst[left]<=target:
                left+=1
            return left
        ret=[0]*len(queries)
        for i,item in enumerate(queries):
            cnt=freq(item)
            ret[i]=len(freq_lst)-search(cnt)
        return ret