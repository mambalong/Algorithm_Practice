# from collections import deque
import collections
import itertools


def slidingPuzzle(board):
    R, C = len(board), len(board[0])

    def neighbours(index0):
        d = [[1,3], [0, 2, 4], [1, 5], [0, 4], [3, 1, 5], [4, 2]]
        return d[index0]

    start = tuple(itertools.chain(*board))
    que = collections.deque([(start, start.index(0))])
    seen = {start}
    step = 0
    target = tuple([i for i in range(1, R*C)] + [0])

    while que:
        sz = len(que)
        for i in range(sz):
            cur, index0 = que.popleft()
            if cur == target:
                return step
            for nei in neighbours(index0):
                new_board = list(cur)
                new_board[nei], new_board[index0] = new_board[index0], new_board[nei]
                new_board = tuple(new_board)
                if new_board not in seen:
                    seen.add(new_board)
                    que.append((new_board, nei))
        step += 1
    return -1

print(slidingPuzzle([[3,2,4],[1,5,0]]))
