import functools
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @functools.lru_cache(maxsize=None)
        def probe(pos,mask):
            if pos>=len(nums1):
                return 0
            cur=1
            ret=None
            for i in range(len(nums2)):
                if cur&mask==0:
                    tmp=(nums1[pos]^nums2[i])+probe(pos+1,mask|cur)
                    if ret is None or ret>tmp:
                        ret=tmp
                cur=cur<<1
            return ret
        return probe(0,0)