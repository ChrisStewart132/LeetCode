'''
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
'''
#include <stdio.h>
#include <stdlib.h>

// Comparison function for qsort
int compare(const void *a, const void *b) {
    return ((int*)*((int**)a))[0] - ((int*)*((int**)b))[0];
}

int maxWidthOfVerticalArea(int** points, int pointsSize, int* pointsColSize) {
    // sort **points by x values
    qsort(points, pointsSize, sizeof(points[0]), compare);

    // find the largest difference
    size_t largest = points[1][0] - points[0][0];
    for(size_t i = 2;i < pointsSize; i++){
        size_t diff = points[i][0] - points[i-1][0];
        if(diff > largest){
            largest = diff;
        }
    }
    return largest;
}