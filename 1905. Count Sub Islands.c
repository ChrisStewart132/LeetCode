/*
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
*/
bool isSubIsland(int** grid1, int** grid2, int gridSize, int* gridColSize, int y, int x){
    bool inBounds = y >= 0 && y < gridSize && x >= 0 && x < gridColSize[y];
    if(!inBounds || grid2[y][x] == 0){
        return true;
    }
    bool output = grid2[y][x] == grid1[y][x];
    grid2[y][x] = 0;// remove sub-island
    bool up = isSubIsland(grid1, grid2, gridSize, gridColSize, y-1, x);
    bool down = isSubIsland(grid1, grid2, gridSize, gridColSize, y+1, x);
    bool left = isSubIsland(grid1, grid2, gridSize, gridColSize, y, x-1);
    bool right = isSubIsland(grid1, grid2, gridSize, gridColSize, y, x+1);
    return output && up && down && left && right;
}
int countSubIslands(int** grid1, int grid1Size, int* grid1ColSize, int** grid2, int grid2Size, int* grid2ColSize) {
    int count = 0;
    for(int y = 0; y < grid2Size; y++){
        for(int x = 0; x < grid2ColSize[y]; x++){
            if(grid2[y][x] == 1 && isSubIsland(grid1, grid2, grid2Size, grid2ColSize, y, x)){
                count++;
            }
        }
    }
    return count;    
}