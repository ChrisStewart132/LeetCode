'''
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.
'''
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        result = 0
        sorted_costs = sorted(costs, reverse=True)
        while len(sorted_costs) > 0 and coins > 0:
            if coins - sorted_costs[-1] < 0:
                break
            else:
                coins -= sorted_costs.pop()
                result += 1
        return result


        