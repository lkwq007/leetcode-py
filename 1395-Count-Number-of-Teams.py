class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # brute force
        ret=0
        for i in range(1,len(rating)-1):
            left_small=0
            left_large=0
            right_small=0
            right_large=0
            cur=rating[i]
            for j in range(i):
                if rating[j]<cur:
                    left_small+=1
                elif rating[j]>cur:
                    left_large+=1
            for j in range(i+1,len(rating)):
                if rating[j]<cur:
                    right_small+=1
                elif rating[j]>cur:
                    right_large+=1
            ret+=left_large*right_small+left_small*right_large
        return ret