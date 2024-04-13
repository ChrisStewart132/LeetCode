/*
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
*/
void removeArea(int** grid, int gridSize, int* gridColSize, int y, int x){
    bool inBounds = y >= 0 && y < gridSize && x >= 0 && x < gridColSize[y];
    if(!inBounds || grid[y][x] == 0){
        return;
    }
    grid[y][x] = 0;
    removeArea(grid, gridSize, gridColSize, y-1, x);
    removeArea(grid, gridSize, gridColSize, y+1, x);
    removeArea(grid, gridSize, gridColSize, y, x-1);
    removeArea(grid, gridSize, gridColSize, y, x+1);
}

int numEnclaves(int** grid, int gridSize, int* gridColSize) {
    // remove all areas on the border
    for(int i = 0; i < gridSize; i++){
        removeArea(grid, gridSize, gridColSize, i, 0);                  // left col
        removeArea(grid, gridSize, gridColSize, i, gridColSize[i]-1);   // right col
    }
    for(int j = 0; j < gridColSize[0]; j++){
        removeArea(grid, gridSize, gridColSize, 0, j);                  // top row
        removeArea(grid, gridSize, gridColSize, gridSize-1, j);         // bottom row
    }
    // return the remaining areas within the boundary
    int output = 0;
    for(int i = 1; i < gridSize-1; i++){
        for(int j = 1; j < gridColSize[i]-1; j++){
            if(grid[i][j] == 1){
                output++;
            }
        }
    }
    return output;
}