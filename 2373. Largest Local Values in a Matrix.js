/*
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

    maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.

In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
*/
/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
function _in_bounds(grid, i, j){
    return i >= 0 && j >= 0 && i < grid.length && j < grid[0].length
}
function _local_max(grid, i, j){
    let max = grid[i][j]
    for(let y = i-1; y < i+2; y++){
        for(let x = j-1; x < j+2; x++){
            if(_in_bounds(grid, y, x))
                max = grid[y][x] > max ? grid[y][x] : max
        }
    }
    return max
}
var largestLocal = function(grid) {
    let output = []
    console.log(grid.length, grid[0].length)
    for(let i=1; i < grid.length-1; i++){
        output.push([])
        for(let j=1; j < grid[0].length-1; j++){
            output[i-1].push(_local_max(grid, i, j))
        }
    }
    return output
};