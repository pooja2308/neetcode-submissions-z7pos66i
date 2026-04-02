class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import numpy as np
        arr = np.array(matrix)
        for ar in np.nditer(arr):
            if ar == target:
                return True
        return False
        