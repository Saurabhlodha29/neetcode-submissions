class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        r = 0
        l = 0
        longest = 0
        substr = set()

        while r < len(s):

            if s[r] in substr:
                while s[l] != s[r]:
                    substr.discard(s[l])
                    l += 1
                substr.discard(s[l])
                l += 1
            
            
            substr.add(s[r])
            r += 1
            longest = max(r-l,longest)

        return longest