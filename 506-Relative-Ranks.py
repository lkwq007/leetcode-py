class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        record=list(map(lambda x,y:(x,y),range(0,len(nums)),nums))
        record.sort(key=lambda x:x[1],reverse=True)
        result=[None]*len(nums)
        medal={
            0:"Gold Medal", 
            1:"Silver Medal", 
            2:"Bronze Medal"
        }
        for no, item in enumerate(record,0):
            no=str(no+1) if no>2 else medal[no]
            result[item[0]]=no
        return result