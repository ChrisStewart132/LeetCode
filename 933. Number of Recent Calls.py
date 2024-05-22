'''
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

    RecentCounter() Initializes the counter with zero recent requests.
    int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
'''
class RecentCounter(object):
    def __init__(self):
        self.requests = []
        self.i = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        delta_t = abs(t - self.requests[self.i])
        while delta_t > 3000 and self.i < len(self.requests):
            self.i += 1
            delta_t = abs(t - self.requests[self.i])
        return len(self.requests) - self.i

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)