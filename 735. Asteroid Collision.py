'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(asteroids)):
            if len(output) == 0:
                output.append(asteroids[i])
                continue

            a = output[-1]
            b = asteroids[i]  
            if a > 0 and b < 0:# collision
                b_alive = True
                # b collides until it is destroyed
                while len(output) > 0 and b_alive:
                    a = output[-1]
                    if a < 0:# collision still occuring
                        break
                    if abs(a) == abs(b):# both explode
                        output.pop()
                        b_alive = False
                    elif abs(a) < abs(b):# a explodes, continue
                        output.pop()
                    else:# b explodes
                        b_alive = False    
                         
                # if b destroyed all previous asteroids
                if b_alive:
                    output.append(b)   
            else:
                output.append(b)
                
        return output
        


