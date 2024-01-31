/*
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
*/
# define MAX_COST 101

int min(int* arr, int n){
    int smallest = arr[0];
    for(int i = 1; i < n; i++){
        if(arr[i] < smallest){
            smallest = arr[i];
        }
    }
    return smallest;
}

int minFallingPathSum(int** matrix, int matrixSize, int* matrixColSize) {
    // nth row[i] cost = min(NW,N,NE) + self
    for(int i = 1; i < matrixSize; i++){// row
        for(int j = 0; j < matrixColSize[i]; j++){// col
            int parents[3] = {matrix[i-1][j]+MAX_COST, matrix[i-1][j], matrix[i-1][j]+MAX_COST};
            if(j > 0){
                parents[0] = matrix[i-1][j-1];
            }
            if(j+1 < matrixColSize[i]){
                parents[2] = matrix[i-1][j+1];
            }
            matrix[i][j] += min(parents, 3);
        }
    }

    // return min last row
    return min(matrix[matrixSize-1], matrixColSize[matrixSize-1]);
}