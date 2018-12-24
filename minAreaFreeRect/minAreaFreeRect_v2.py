# ===================================================================================
# https://leetcode.com/problems/minimum-area-rectangle-ii/
# Accepted
# ===================================================================================

import collections
import itertools
import math
import sys

class Solution(object):
    def minAreaFreeRect(self, points):
        """
    :type points: List[List[int]]
    :rtype: float
    """

        # ===================================================================================
        # Calculate the direction of each two points from the input file.
        # And use defaultdict to aggregate paris that have same direction
        # ===================================================================================
        twoPointsCombination = itertools.combinations(points,2)
        twoPointMap = collections.defaultdict(list)
        for p1,p2 in twoPointsCombination:
            direction = (p2[0] - p1[0],p2[1] - p1[1])
            if direction[0]<0 or (direction[0] == 0 & direction[1]<0):
                # Make sure the direction is same
                direction = (-direction[0],-direction[1])
                twoPointMap[direction].append((p2, p1))
            else:
                twoPointMap[direction].append((p1, p2))


        res = math.inf
        # ===================================================================================
        # Then we loop through all directions that have more than one pairs.
        # And check the direction between two paris is orthogonal.
        # If yes, the two paris form a rectangle
        # ===================================================================================
        for direction, pairs in twoPointMap.items():
            if len(pairs) > 1:
                for i in range(0, len(pairs) - 1):
                    p1, p2 = pairs[i]
                    for j in range(i + 1, len(pairs)):
                        p3 = pairs[j][0]
                        direction_2 = (p3[0] - p1[0], p3[1] - p1[1])
                        if abs(direction_2[0] * direction[0] + direction_2[1] * direction[1]) < 1e-5:
                            area = math.sqrt(math.pow(direction_2[0], 2) + math.pow(direction_2[1], 2)) * \
                                   math.sqrt(math.pow(direction[0], 2) + math.pow(direction[1], 2))
                            res = min(res, area)
        if res == math.inf:
            return 0.0
        else:
            return res


if __name__ == '__main__':
    model = Solution()

    test5 = [[1,2],[2,1],[1,0],[0,1]]
    print(model.minAreaFreeRect(test5))