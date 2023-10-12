'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
'''
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs_backtrack(output, is_solution, add_to_output, children, candidate=[]):
            if is_solution(candidate):
                add_to_output(candidate)
            else:
                for child_candidate in children(candidate):
                    dfs_backtrack(output, is_solution, add_to_output, children, child_candidate)
                    
        def combinations(desired_length, n, starting_candidate):
            def is_solution(candidate):
                return len(candidate) == desired_length
            
            def add_to_output(candidate):
                output.append(candidate[:])  # Append a copy of the candidate to avoid modifying it later.
                
            def children(candidate):
                output = []
                last_used = candidate[-1] if candidate else 0
                for x in range(last_used + 1, n + 1):
                    if x not in candidate:
                        output.append(candidate + [x])
                return output
            
            output = []
            dfs_backtrack(output, is_solution, add_to_output, children, starting_candidate)
            return output

        return combinations(k, n, [])
