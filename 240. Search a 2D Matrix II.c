/*
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

*/
bool binSearch(int* arr, int arrSize, int target){
    int l = 0;
    int r = arrSize-1;
    while(l < r){
        int m = l + (r-l)/2;
        if(arr[m] == target){
            return true;
        }else if(target < arr[m]){
            r = m-1;
        }else{
            l = m+1;
        }
    }
    return arr[l] == target;
}

bool _searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target, int y, int x){
    if(y == matrixSize-1){
        //printf("searching bottom row\n");
        return binSearch(matrix[y], matrixColSize[y], target);
        
    }else if(x == 0){
        //printf("searching left col\n");
        if(matrix[y][x] == target){
            return true;
        }
        return y < matrixSize && _searchMatrix(matrix, matrixSize, matrixColSize,target, y+1, x);
    }else if(matrix[y][x] == target){
        return true;
    }else if(target < matrix[y][x]){
        return _searchMatrix(matrix, matrixSize, matrixColSize,target, y, x-1);
    }else{
        return _searchMatrix(matrix, matrixSize, matrixColSize,target, y+1, x);
    }
}

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int y = 0;
    int x = matrixColSize[matrixSize-1]-1;
    return _searchMatrix(matrix, matrixSize, matrixColSize,target, y, x);
}