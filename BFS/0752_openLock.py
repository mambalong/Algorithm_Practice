def plusOne(s, j):
    re = [int(i) for i in s]
    if re[j] == 9:
        re[j] = 0
    else:
        re[j] += 1
    return ''.join(list(map(str, re)))

def minusOne(s, j):
    re = [int(i) for i in s]
    if re[j] == 0:
        re[j] = 9
    else:
        re[j] -= 1
    return ''.join(list(map(str, re)))

def bfs(deadends, target):
    deadends = set(deadends)
    q1 = set(['0000'])
    q2 = set([target])
    visited = set()
    step = 0
    while q1 and q2:
        if len(q1) > len(q2):
            q1, q2 = q2, q1
        tmp = set()
        for cur in q1:
            if cur in deadends:
                continue
            if cur in q2:
                return step
            visited.add(cur)
            for j in range(4):
                up = plusOne(cur, j)
                if up not in visited:
                    tmp.add(up)
                down = minusOne(cur, j)
                if down not in visited:
                    tmp.add(down)
        step += 1
        q1 = tmp

    return -1
print(bfs(["0201","0101","0102","1212","2002"], '0202'))