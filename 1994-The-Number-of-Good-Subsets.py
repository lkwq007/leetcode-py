class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        # TLE
        primes=[2,3,5,7,11,13,17,19,23,29]
        mask=1
        acc=0
        mapping=[0]*31
        for i in range(1,30):
            if i in primes:
                acc=acc|mask
            mapping[i]=mask
            mask=mask<<1
        for i in range(len(primes)):
            for j in range(i+1,len(primes)):
                val=primes[i]*primes[j]
                if 1<=val<=30:
                    mapping[val]=mapping[primes[i]]|mapping[primes[j]]
        for item in [2,3,5]:
            mapping[30]=mapping[30]|mapping[item]
        ret=0
        term=10**9+7
        record={}
        cnt=0
        count=[0]*31
        for item in nums:
            count[item]+=1
        for i in range(2,31):
            if count[i]==0:
                continue
            mask=mapping[i]
            # print(item,bin(mask),bin(mask|acc),bin((mask|acc)^acc))
            if (mask|acc)^acc==0:
                for key in list(record.keys()):
                    if mask&key==0:
                        record[key|mask]=(record.get(key|mask,0)+record[key]*count[i])%term
                record[mask]=(record.get(mask,0)+count[i])%term
        # print(record)
        for _,v in record.items():
            ret=ret+v
            ret%=term
        for i in range(count[1]):
            ret=(ret+ret)%term
        return ret
