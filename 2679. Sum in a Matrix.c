/*
You are given a 0-indexed 2D integer array nums. Initially, your score is 0. Perform the following operations until the matrix becomes empty:

    From each row in the matrix, select the largest number and remove it. In the case of a tie, it does not matter which number is chosen.
    Identify the highest number amongst all those removed in step 1. Add that number to your score.

Return the final score.
*/
void swap(int* nums, int i, int j){
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
bool compare(int a, int b){
    return a > b;
}
void siftDown(int* heap, int heapSize, int p){
    if(p >= heapSize){
        return;
    }
    int smallest = p;
    int nChildren = 2;// binary heap
    for(int c = p*2+1; c < heapSize && c < p*2+1+nChildren; c++){
        smallest = compare(heap[smallest], heap[c]) ? smallest : c;
    }
    if(smallest != p){
        swap(heap, p, smallest);
        siftDown(heap, heapSize, smallest);
    }
}
void heapify(int* nums, int numsSize){
    for(int p = numsSize/2 + numsSize%2 - 1; p > -1; p--){
        siftDown(nums, numsSize, p);
    }
}
int pop(int* heap, int heapSize){
    swap(heap, 0, heapSize-1);
    siftDown(heap, heapSize-1, 0);
    return heap[heapSize-1];
}

int max(int a, int b){
    return a>b?a:b;
}

int matrixSum(int** nums, int numsSize, int* numsColSize){
    for(int i = 0; i < numsSize; i++){
        heapify(nums[i], numsColSize[i]);
    }
    
    int longestRow = numsColSize[0];
    for(int i = 0; i < numsSize; i++){
        longestRow = longestRow > numsColSize[i] ? longestRow : numsColSize[i]; 
    }

    int output = 0;
    for(int i = 0; i < longestRow; i++){
        int largest = 0;
        for(int j = 0; j < numsSize; j++){
            if(numsColSize[j] > 0){
                largest = max(largest, pop(nums[j], numsColSize[j]--));
            }
        }
        output += largest;
    }
    return output;
}   