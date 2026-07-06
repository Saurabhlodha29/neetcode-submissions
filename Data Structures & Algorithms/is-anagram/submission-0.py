class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = dict()
        dict2 = dict()

        for char in s:
            if char in dict1:
                dict1[char] = dict1[char] + 1
            else:
                dict1[char] = 1

        for char in t:
            if char in dict2:
                dict2[char] = dict2[char] + 1
            else:
                dict2[char] = 1

        for char in dict1.keys():
            if char not in dict2.keys():
                return False
            if char in dict2.keys():
                if dict1[char] != dict2[char]:
                    return False

        return True
        