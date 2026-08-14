class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, (rows * cols) - 1

        while l <= r:
            mid = (l + r)//2
            
            rm = mid // cols
            cm = mid % cols

            if matrix[rm][cm] > target:
                r = mid - 1
            elif matrix[rm][cm] < target:
                l = mid + 1
            else:
                return True

        return False