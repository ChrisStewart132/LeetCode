/*
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
*/

int islandArea(int** grid, int gridSize, int* gridColSize, int y, int x){
    // returns the area of the island and removes it from the grid
    bool inBounds = y >= 0 && y < gridSize && x >= 0 && x < gridColSize[y];
    if(!inBounds){
        return 0;
    }
    if(grid[y][x] == 0){
        return 0;
    }
    grid[y][x] = 0;
    int up = islandArea(grid, gridSize, gridColSize, y-1, x);
    int down = islandArea(grid, gridSize, gridColSize, y+1, x);
    int left = islandArea(grid, gridSize, gridColSize, y, x-1);
    int right = islandArea(grid, gridSize, gridColSize, y, x+1);
    int area = 1 + up + down + left + right;
    return area;
}

int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize) {
    int largestArea = 0;
    for(int y = 0; y < gridSize; y++){
        for(int x = 0; x < gridColSize[y]; x++){
            int area = 0;
            if(grid[y][x] == 1){
                area = islandArea(grid, gridSize, gridColSize, y, x);
            }
            largestArea = largestArea > area ? largestArea : area;
        }
    }
    return largestArea;    
}