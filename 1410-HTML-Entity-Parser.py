class Solution:
    def entityParser(self, text: str) -> str:
        ret=""
        cache=""
        table={
            "&quot;":'"',
            "&apos;": "'",
            "&amp;" : "&",
            "&gt;" : ">",
            "&lt;" : "<",
            "&frasl;" : "/",
        }
        for item in text:
            if cache:
                if item=="&":
                    ret+=cache
                    cache="&"
                elif item==";":
                    cache+=";"
                    ret+=table.get(cache,cache)
                    cache=""
                else:
                    cache+=item
            elif item=="&":
                cache="&"
            else:
                ret+=item
        return ret