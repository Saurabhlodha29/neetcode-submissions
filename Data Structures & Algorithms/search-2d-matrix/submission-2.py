class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            if matrix[i][-1] > target:
                break
            elif matrix[i][-1] == target:
                return True
        
        st = 0
        end = len(matrix[i]) - 1

        while st <= end:
            mid = (end+st)//2
            if matrix[i][mid] < target:
                st = mid+1
            elif matrix[i][mid] > target:
                end = mid-1
            else:
                return True

        return False