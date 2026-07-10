class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if j == i:
                    continue
                elif numbers[j] == target - numbers[i]:
                    return [min(i+1,j+1),max(i+1,j+1)]
                elif j > target - numbers[i]:
                    break

            