class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        numIslands = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.search(i, j, grid, visited)
                    numIslands += 1
                else:
                    visited.add((i, j))
        
        return numIslands
    
    def search(self, i, j, grid, visited):
        
        visited.add((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in directions:
            newI, newJ = i + x, j + y

            if 0 <= newI < len(grid) and 0 <= newJ < len(grid[0]):
                if grid[newI][newJ] == "1" and (newI, newJ) not in visited:
                    self.search(newI, newJ, grid, visited)
        
        return
        