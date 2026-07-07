class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            countList = [0]*26
            for char in s:
                countList[ord(char) - ord('a')] += 1
            key = tuple(countList)

            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return list(groups.values())