inp = input('Please input the size of the matrix (eg. 49): ')
m = int(inp[0])
n = int(inp[1])

def n2let(n):
    if n > 26:
        n %= 26
    return chr(ord('A') + (n-1))


k, i, j = 1, 1, 1
ans = [[0]*(n+2) for i in range(m+2)]
ans[1][1] = 'A'
while k < m*n:
    # right
    while j < n and not ans[i][j+1]:
        k += 1
        j += 1
        ans[i][j] = n2let(k)

    # down
    while i < m and not ans[i+1][j]:
        k += 1
        i += 1
        ans[i][j] = n2let(k)
        
    # left
    while j > 1 and not ans[i][j-1]:
        k += 1
        j -= 1
        ans[i][j] = n2let(k)

    # up
    while i > 1 and not ans[i-1][j]:
        k += 1
        i -= 1
        ans[i][j] = n2let(k)
print('ass')

print(ans)