class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        diff0=[0]*len(security)
        diff1=[0]*len(security)
        for i in range(1,len(security)):
            if security[i]<security[i-1]:
                diff0[i-1]=1
            elif security[i]>security[i-1]:
                diff1[i-1]=1
            else:
                diff0[i-1]=diff1[i-1]=1
            diff0[i-1]+=diff0[i-2]
            diff1[i-1]+=diff1[i-2]
        # print(diff0)
        # print(diff1)
        ret=[]
        for i in range(time-1,len(security)-time-1):
            if diff0[i]-diff0[i-time]==time and diff1[i+time]-diff1[i]==time:
                ret.append(i+1)
        return ret