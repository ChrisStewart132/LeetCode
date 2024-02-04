/*
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
*/
int min(int a, int b){
    return a<b?a:b;
}
int minCostClimbingStairs(int* cost, int costSize) {
    for(int i = 2; i < costSize; i++){
        cost[i] += min(cost[i-1], cost[i-2]);
    }
    return min(cost[costSize-1], cost[costSize-2]);
}