class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        lst=[abs(nums1[i]-nums2[i]) for i in range(len(nums1))]
        k=k1+k2
        record={0:0}
        for item in lst:
            record[item]=record.get(item,0)+1
        keys=sorted(record.keys(),reverse=True)
        ret=0
        for i in range(len(keys)):
            key=keys[i]
            val=record[key]
            if k==0:
                ret+=val*key*key
            else:
                next=keys[i+1] if i+1<len(keys) else 0
                diff=(key-next)*val
                if diff<=k:
                    k-=diff
                    record[next]=record.get(next,0)+val
                else:
                    cut=k//val
                    rest=k%val
                    ret+=(val-rest)*(key-cut)*(key-cut)
                    ret+=(rest)*(key-cut-1)*(key-cut-1)
                    k=0
        return ret