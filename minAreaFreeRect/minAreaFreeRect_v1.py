# ===================================================================================
# https://leetcode.com/problems/minimum-area-rectangle-ii/
# Below code got timeout error when submit
# ===================================================================================


import itertools
import math


class Solution(object):
    def minAreaFreeRect(self, points):
        """
    :type points: List[List[int]]
    :rtype: float
    """
        MAX_DISTIANCE = 40001
        funDistance = lambda point1,point2: math.sqrt( math.pow(point1[0] - point2[0],2) +  math.pow(point1[1] - point2[1],2))
        threePointsCombination = itertools.combinations(points,3)
        threeIndexList = list(itertools.combinations(range(3),2))
        min_area = MAX_DISTIANCE*MAX_DISTIANCE
        for threePoint in threePointsCombination:
            all_distances = []
            for i,j in threeIndexList:
                all_distances.append(funDistance(threePoint[i],threePoint[j]))
            sorted_index = [i[0] for i in sorted(enumerate(all_distances), key=lambda x: x[1])]
            sd,md,ld = (all_distances[sorted_index[i]] for i in range(3))
            if sd+md <= ld:
                continue
            if abs(math.pow(sd,2) + math.pow(md,2) - math.pow(ld,2)) > 1e-5:
                continue
            short_points = [i for i in threeIndexList[sorted_index[0]]]
            long_points = [i for i in threeIndexList[sorted_index[-1]]]
            cp = [i for i in long_points if i in short_points][0]
            sp = [i for i in short_points if i != cp][0]
            lp = [i for i in long_points if i != cp][0]

            direction = [threePoint[cp][i] - threePoint[sp][i] for i in range(2)]
            new_point = [threePoint[lp][i] + direction[i] for i in range(2)]
            if new_point in points:
                #print([threePoint[cp],threePoint[sp],threePoint[lp],new_point])
                area = all_distances[sorted_index[0]] * all_distances[sorted_index[1]]
                if area < min_area:
                    min_area = area

        if min_area == MAX_DISTIANCE*MAX_DISTIANCE:
            return 0.0
        else:
            return min_area


if __name__ == '__main__':
    model = Solution()
    test1 = [[1,2],[2,1],[1,0],[0,1]]
    print(model.minAreaFreeRect(test1))

    test2 = [[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]]
    print(model.minAreaFreeRect(test2))

    test3 = [[0,3],[1,2],[3,1],[1,3],[2,1]]
    print(model.minAreaFreeRect(test3))

    test4 = [[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]
    print(model.minAreaFreeRect(test4))