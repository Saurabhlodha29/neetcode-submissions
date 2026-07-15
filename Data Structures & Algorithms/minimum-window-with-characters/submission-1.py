class Solution:
    def minWindow(self, s: str, t: str) -> str:

        check = {}

        for c in t:
            check[c] = check.get(c, 0) + 1

        window = {}

        have = 0
        need = len(check)

        l = 0

        res = [-1, -1]
        resLen = float("inf")

        for r in range(len(s)):

            c = s[r]

            window[c] = window.get(c, 0) + 1

            if c in check and window[c] == check[c]:
                have += 1

            while have == need:

                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1

                if s[l] in check and window[s[l]] < check[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l:r+1] if resLen != float("inf") else ""