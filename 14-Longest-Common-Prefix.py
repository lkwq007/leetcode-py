class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<1:
            return ""
        end=1
        while True:
            if end<=len(strs[0]):
                prefix=strs[0][:end]
            for item in strs:
                if end<=len(item) and prefix==item[:end]:
                    continue
                return strs[0][:end-1]
            end+=1
        return ""