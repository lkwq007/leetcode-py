class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # it seem that we need to use dynamic programming
        if not text1 or not text2:
            return 0
        len1=len(text1)
        len2=len(text2)
        template=[0]*(len2+1)
        table=[None]*(len1+1)
        for idx in range(0,len1+1):
            table[idx]=template[:]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if text1[i-1]==text2[j-1]:
                    table[i][j]=table[i-1][j-1]+1
                else:
                    table[i][j]=max(table[i-1][j],table[i][j-1])
        return table[len1][len2]