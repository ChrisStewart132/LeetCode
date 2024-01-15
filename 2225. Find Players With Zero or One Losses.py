'''
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:

    You should only consider the players that have played at least one match.
    The testcases will be generated such that no two matches will have the same outcome.
'''
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        undefeated = []
        lost_once = []
        cache = {}# player->n_losses

        players = set()
        for w,l in matches:
            players.add(w)
            try:
                cache[l] += 1
            except KeyError:
                cache[l] = 1

        for player in players:
            if player not in cache:
                undefeated.append(player)

        for player, n_losses in cache.items():
            if(n_losses == 0):
                undefeated.append(player)
            if(n_losses == 1):
                lost_once.append(player)

        return sorted(undefeated), sorted(lost_once)