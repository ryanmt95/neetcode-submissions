class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        left, right = 0, len(matrix)-1
        rowIndex = -1

        while left <= right:
            index = (left+right)//2

            if matrix[index][0] <= target <= matrix[index][-1]:
                rowIndex = index
                break
            
            if target > matrix[index][0]:
                left = index + 1
            else:
                right = index - 1
        
        if rowIndex == -1:
            return False
        
        left, right = 0, len(matrix[0]) - 1
        while left <= right: 
            index = (left+right)//2
            val = matrix[rowIndex][index]

            if val == target:
                return True
            
            if target > val:
                left = index + 1
            else:
                right = index - 1
        
        return False
