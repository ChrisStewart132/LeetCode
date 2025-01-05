/*
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
*/
void removeArea(char** grid, int gridSize, int* gridColSize, int y, int x){
    bool inBounds = y >= 0 && y < gridSize && x >= 0 && x < gridColSize[y];
    if(!inBounds || grid[y][x] == '0'){
        return;
    }
    grid[y][x] = '0';
    removeArea(grid, gridSize, gridColSize, y-1, x);
    removeArea(grid, gridSize, gridColSize, y+1, x);
    removeArea(grid, gridSize, gridColSize, y, x-1);
    removeArea(grid, gridSize, gridColSize, y, x+1);
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int nIslands = 0;
    for(int i = 0; i < gridSize; i++){
        for(int j = 0; j < gridColSize[i]; j++){
            if(grid[i][j] == '1'){
                removeArea(grid, gridSize, gridColSize, i, j);
                nIslands++;
            }
        }
    }
    return nIslands;
}