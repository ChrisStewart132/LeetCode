/*
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
 and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
 One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
*/
int nNeighbours(int** grid, int gridSize, int* gridColSize, int i, int j){
    int u = i-1 >= 0? grid[i-1][j] : 0;
    int d = i+1 < gridSize? grid[i+1][j] : 0;
    int l = j-1 >= 0? grid[i][j-1] : 0;
    int r = j+1 < gridColSize[i]? grid[i][j+1] : 0;
    return u+d+l+r;
}
int islandPerimeter(int** grid, int gridSize, int* gridColSize) {
    // total perimeter = n_sqares*4 - 1*square[i] foreach neighbour
    int perimeter = 0;
    for(int i = 0; i < gridSize; i++){
        for(int j = 0; j < gridColSize[i]; j++){
            if(grid[i][j]){
                perimeter += 4;
                perimeter -= nNeighbours(grid, gridSize, gridColSize, i, j);
            }
        }
    }
    return perimeter;
}