class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        record={}
        total=len(votes[0])
        for item in votes[0]:
            record[item]=[0]*total
            record[item].append(item)
        for vote in votes:
            for i,item in enumerate(vote,0):
                record[item][i]-=1
        keys=list(record.keys())
        keys.sort(key=lambda x:tuple(record[x]))
        return "".join(keys)