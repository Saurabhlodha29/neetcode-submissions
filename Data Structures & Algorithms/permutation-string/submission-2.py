class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        check = [0] * 26
        for c in s1:
            check[ord(c)-ord('a')] += 1

        l = 0
        r = l+len(s1)-1

        window = [0] * 26
        for c in range(l,r+1):
            window[ord(s2[c])-ord('a')] += 1

        while r+1 < len(s2):
            if window == check:
                return True

            else:
                r+=1
                l+=1
                window[ord(s2[l-1])-ord('a')] -= 1
                window[ord(s2[r])-ord('a')] += 1

        return window == check
            


        

        



        