class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = 0
        end = len(s)-1

        while st < end:
            if not (s[st].isalnum()):
                st += 1
            elif not (s[end].isalnum()):
                end -= 1

            elif s[st].lower() == s[end].lower():
                st += 1
                end -= 1
            else:
                return False

        return True
