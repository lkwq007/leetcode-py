class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt=0
        for idx in range(0,len(startTime)):
            if startTime[idx]<=queryTime<=endTime[idx]:
                cnt+=1
        return cnt