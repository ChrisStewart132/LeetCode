'''
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
'''
class Solution(object):
    def _restoreIpAddresses(self, s, i=1, depth=0):
        """generate addresses"""
        output = []
        for j in range(i,i+3):
            candidate = (s[:j] + '.' + s[j:])
            if depth < 2:
                output += self._restoreIpAddresses(candidate, j+2, depth+1)
            else:
                output.append(candidate)          
        return output

    def addr_valid(self, addr, depth=0):     
        if depth == 3:
            return len(addr) > 0 and int(addr) <= 255 and not(len(addr) > 1 and addr[0] == '0')

        i = addr.index('.')# index of next '.'
        if i > 3 or i == 0 or (i > 1 and addr[0] == '0'):
            return False

        n = int(addr[:i])# byte number
        if not(0 <= n <= 255):# byte number valid
            return False
        return self.addr_valid(addr[i+1:], depth+1)

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        candidates = [x for x in self._restoreIpAddresses(s)]
        output = [x for x in candidates if self.addr_valid(x)]
        return set(output)
