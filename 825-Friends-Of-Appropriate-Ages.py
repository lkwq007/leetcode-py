class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        record={}
        ret=0
        for item in ages:
            record[item]=record.get(item,0)+1
        keys=sorted(record.keys())
        left=0
        acc=0
        for i in range(len(keys)):
            while left<len(keys) and keys[left]<=keys[i]//2+7:
                acc-=record[keys[left]]
                left+=1
            acc+=record[keys[i]]
            if left<len(keys) and keys[left]<=keys[i]:
                ret+=record[keys[i]]*acc-record[keys[i]]
        return ret

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        record={}
        for item in ages:
            record[item]=record.get(item,0)+1
        ret=0
        for k,v in record.items():
            if v>1 and k>14:
                ret+=v*(v-1)//2
        ages.sort()
        for i in range(len(ages)):
            val=ages[i]//2+7
            left=0
            right=i
            while left<right:
                middle=left+(right-left)//2
                if ages[middle]<=val:
                    left=middle+1
                else:
                    right=middle
            ret+=i-left
        return ret