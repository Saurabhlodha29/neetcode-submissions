class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "".join(f"{len(s)}#{s}" for s in strs)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_string = list()
        nums = set(['0','1','2','3','4','5','6','7','8','9'])
        length = 0
        i = 0
        while i < len(s):
            if s[i] in nums:
                length = 10*length + int(s[i])
                if s[i+1] in nums:
                    i += 1
                elif s[i+1] == '#':
                    i += 1
                    decoded_string.append(s[i+1:i+length+1])
                    i = i+length+1
                    length = 0

        return decoded_string
