/*
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

    The number of soldiers in row i is less than the number of soldiers in row j.
    Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
*/
void swap(int** nums, int i, int j){
    int* temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
bool compare(int* a, int* b){
    return a[0] == b[0] && a[1] < b[1] || a[0] < b[0];
}
void siftDown(int** heap, int heapSize, int p){
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
void heapify(int** nums, int numsSize){
    for(int p = numsSize/2 + numsSize%2 - 1; p > -1; p--){
        siftDown(nums, numsSize, p);
    }
}
int pop(int** heap, int heapSize){
    swap(heap, 0, heapSize-1);
    siftDown(heap, heapSize-1, 0);
    return heap[heapSize-1][1];
}

int search(int* arr, int r){
    if(arr[r-1]==1){
        return r;
    }
    int l = 0;
    while(l<=r){
        int m = l+(r-l)/2;
        if(arr[m]==1){
            l=m+1;
        }else{
            r=m-1;
        }
    }
    return arr[l]==0?l:-1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* kWeakestRows(int** mat, int matSize, int* matColSize, int k, int* returnSize) {
    // heapify keys based on key=lambda x : (count[x], x)
    int** heap = (int**)malloc(sizeof(int*)*matSize);
    for(int i =0; i < matSize; i++){
        heap[i] = (int*)malloc(sizeof(int)*2);
        heap[i][0] = search(mat[i], matColSize[i]);
        heap[i][1] = i;
    }
    heapify(heap, matSize);    

    *returnSize = k;
    int* output = (int*)malloc(sizeof(int)*returnSize[0]);
    

    // get k weakest
    for(int i = 0; i < k; i++){
        output[i] = pop(heap, matSize-i);
    }

    for(int i =0; i < matSize; i++){
        free(heap[i]);
    }
    free(heap);

    return output;
}