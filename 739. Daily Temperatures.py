'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
class Solution(object):
    def dailyTemperatures(self, temperatures, i=0, output=None):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if output == None:
            output = [0 for x in temperatures]

        if i == len(temperatures):# end of array
            return 

        self.dailyTemperatures(temperatures, i+1, output)

        result = 1
        j = i+1

        while j < len(temperatures):       
            if temperatures[j] > temperatures[i]:            
                output[i] = result
                return output
            elif output[j] > 0:
                result += output[j]
                j += output[j]              
            else:
                break
       
        output[i] = 0
        return output


    