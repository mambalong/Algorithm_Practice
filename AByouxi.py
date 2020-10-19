import sys
from collections import deque
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        s = line.split(' ')
        A = int(s[0])
        B = int(s[1])

        def minus(tup):
            res = []
            a, b = tup[0], tup[1]
            # a
            tmp = a - b
            if tmp > 0:
                res.append((tmp, b))
            # b
            tmp = b - a
            if tmp > 0:
                res.append((a, tmp))
            return res
        
        def divide(tup):
            res = []
            a, b = tup[0], tup[1]
            # a
            tmp = a // b
            if tmp > 0:
                res.append((tmp, b))
            # b
            tmp = b // a
            if tmp > 0:
                res.append((a, tmp))
            return res
        
        def bfs(A, B):
            start = (A, B)
            target = (1, 1)
            que = deque([start])
            seen = {start}

            step = 0

            while que:
                sz = len(que)
                for i in range(sz):
                    cur = que.popleft()
                    if cur == target:
                        return step
                    neighbours = []
                    neighbours += divide(cur)
                    neighbours += minus(cur)

                    for nei in neighbours:
                        if nei not in seen:
                            seen.add(nei)
                            que.append(nei)
                step += 1
            return -1
        
        print(bfs(A, B))

        