class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            numMap = defaultdict(int)
            for num in row:
                if num.isdigit():
                    numMap[num] += 1

                if numMap[num] > 1:
                    return False
        
        for i in range(9):
            numMap = defaultdict(int)
            for j in range(9):
                num = board[j][i]

                if num.isdigit():
                    numMap[num] += 1
                
                if numMap[num] > 1:
                    return False

        boxes = []
        for i in range(3):
            x = i * 3
            for j in range(3):
                y = j * 3
                boxes.append((x, y))

        for x, y in boxes:
            print(x, y)
            numMap = defaultdict(int)
            for i in range(3):
                for j in range(3):
                    num = board[x+i][y+j]

                    if num.isdigit():
                        numMap[num] += 1
                    
                    if numMap[num] > 1:
                        return False

        return True