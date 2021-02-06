class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        record={}
        mid=len(encoded)//2
        acc=len(encoded)+1
        ret=[0]*acc
        for i,item in enumerate(encoded,0):
            acc^=(i+1)
            if i<mid and i%2==0 or i>=mid and (len(encoded)-i-1)%2==0:
                acc^=item
        ret[mid]=acc
        for i in range(mid):
            ret[mid-i-1]=ret[mid-i]^encoded[mid-i-1]
            ret[mid+i+1]=ret[mid+i]^encoded[mid+i]
        return ret
'''
perm[0]^perm[1]
perm[1]^perm[2]
perm[2]^perm[3]
perm[3]^perm[4]
perm[1]^perm[2]^perm[3]
'''