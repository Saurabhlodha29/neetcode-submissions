class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = dict()
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        
        for char in t:
            if char in dict1 and dict1[char] != 0:
                dict1[char] -= 1
            else:
                return False

        return all(value == 0  for value in dict1.values())
           
