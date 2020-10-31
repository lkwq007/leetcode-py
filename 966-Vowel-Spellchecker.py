class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        record={}
        cap_record={}
        vowel_record={}
        vowels=set("aeiouAEIOU")
        def replace_vowel(x):
            return "".join([item if item not in vowels else "?" for item in x])
        for word in wordlist:
            record[word]=1
            low=word.lower()
            if low not in cap_record:
                cap_record[low]=word
            # cap_record[low].append(word)
            stem=replace_vowel(low)
            if stem not in vowel_record:
                vowel_record[stem]=word
        def check(word):
            if word in record:
                return word
            low=word.lower()
            if low in cap_record:
                return cap_record[low]
            stem=replace_vowel(low)
            if stem in vowel_record:
                return vowel_record[stem]
            return ""
        return [check(word) for word in queries]