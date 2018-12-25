import collections
import copy

# ===================================================================================
# https://leetcode.com/submissions/detail/196953828/
# Accepted
# ===================================================================================


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        status = self.init(board)
        solution = self.solve(status)
        if solution is not None:
            for (i,j),num in solution['solutions'].items():
                board[i][j] = num


    def init(self, board):
        out = {}
        all_possible_solutions = [str(x) for x in range(1, 10)]
        out['possible_branch'] = []
        out['dict_row'] = collections.defaultdict(list)
        out['dict_col'] = collections.defaultdict(list)
        out['dict_box'] = collections.defaultdict(list)

        # Go through the input board once to collect information
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    out['possible_branch'].append([i, j])
                else:
                    out['dict_row'][i].append(num)
                    out['dict_col'][j].append(num)
                    out['dict_box'][3 * (i // 3) + (j // 3)].append(num)

        # Get all possible elements for each column,row and box
        for k in range(9):
            out['dict_row'][k] = list(set(all_possible_solutions) - set(out['dict_row'][k]))
            out['dict_col'][k] = list(set(all_possible_solutions) - set(out['dict_col'][k]))
            out['dict_box'][k] = list(set(all_possible_solutions) - set(out['dict_box'][k]))

        # Work out all possible numbers for each cell
        out['branches'] = {}
        for (i, j) in out['possible_branch']:
            possible_nums =[]
            for num in out['dict_row'][i]:
                if (num in  out['dict_col'][j])  & (num in out['dict_box'][3 * (i // 3) + (j // 3)]):
                    possible_nums.append(num)
            out['branches'][(i, j)] = possible_nums
        out['solutions'] = {}
        return out

    def solve(self,status):
        # If no branch need go through, we have found the solution!
        if len(status['branches']) ==0: return status

        # Otherwise, we go through each possible elements and check whether the solution is still feasible at this moment
        for (i,j),possible_nums in status['branches'].items():
            for num in possible_nums:
                valid = (num in status['dict_row'][i]) & (num in status['dict_col'][j]) & (num in status['dict_box'][3 * (i // 3) + (j // 3)])
                if not valid:
                    status['branches'][(i, j)].remove(num)
                    # If the current cell do not have any possible scenario to explore, we should cut the branch
                    if len(status['branches'][(i, j)]) == 0:
                        return None

        # Let the algorithm start with the minimum possible cells
        order_list = sorted(status['branches'].keys(), key=lambda x: len(status['branches'][x]))

        for (i,j) in order_list:
            possible_nums = status['branches'][(i, j)]
            for num in possible_nums:
                # Create a new status object, be careful here, we need use deepcopy!
                new_status = copy.deepcopy(status)
                new_status['solutions'][(i,j)] = num
                new_status['branches'].pop((i,j))
                new_status['dict_row'][i].remove(num)
                new_status['dict_col'][j].remove(num)
                new_status['dict_box'][3 * (i // 3) + (j // 3)].remove(num)
                try_solve = self.solve(new_status)
                if try_solve is not None:
                    return try_solve
                else:
                    # This solution has tried, and we don't have try again later
                    status['branches'][(i,j)].remove(num)
                    # Cut the branches if not feasible
                    if len(status['branches'][(i,j)]) == 0:
                        return None

#test_board =[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
test_board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
obj = Solution()
out = obj.solveSudoku(test_board)
print(test_board)