/*
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/
int climbStairs(int n) {
    if(n < 4){
        return n;
    }
    return climbStairs(n-1) + climbStairs(n-2);
}