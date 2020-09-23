class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        ret=[]
        for key,val in record.items():
            if val>len(nums)//3:
                ret.append(key)
        return ret
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        ret=[]
        for key,val in record.items():
            if val>len(nums)//3:
                ret.append(key)
        return ret

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<1:
            return []
        # Boyer–Moore majority vote algorithm
        counter=0
        majority=nums[0]
        tmp=nums[0]
        idx=0
        while idx<len(nums):
            item=nums[idx]
            if item!=majority:
                tmp=item
                break
            else:
                counter+=1
            idx+=1
        if idx>=len(nums):
            return [majority]
        counter=[[majority,counter],[tmp,1]]
        for i in range(idx+1,len(nums)):
            item=nums[i]
            if item==counter[0][0]:
                counter[0][1]+=1
            elif item==counter[1][0]:
                counter[1][1]+=1
            else:
                if counter[0][1]<counter[1][1]:
                    idx=0
                else:
                    idx=1
                counter[idx][1]-=1
                if counter[idx][1]==0:
                    counter[idx][0]=item
                    counter[idx][1]=1
        def validate(x):
            cnt=0
            for item in nums:
                if x==item:
                    cnt+=1
            return cnt>len(nums)//3
        ret=[item[0] for item in counter if validate(item[0])]
        if len(ret)==1:
            cnt=0
            majority=0
            for item in nums:
                if item==ret[0]:
                    continue
                if cnt==0:
                    majority=item
                    cnt=1
                elif majority==item:
                    cnt+=1
                else:
                    cnt-=1
            if validate(majority):
                ret.append(majority)
        return ret