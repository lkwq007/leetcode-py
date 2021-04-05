class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users={}
        ret=[0]*k
        for uid,time in logs:
            if uid not in users:
                users[uid]={}
            users[uid][time]=1
        for _,user in users.items():
            total=len(user)
            if total<=k:
                ret[total-1]+=1
        return ret