# 框架来自力扣 @nettee，仅有些许改动

# 二叉树的 dfs 结构
def dfs(root):
    if root == None:
        return
    dfs(root.left)
    dfs(root.right)

'''
借鉴二叉树的 dfs，我们需要处理 base case 还有访问相邻的节点
网格中一个格子的相邻节点就是上下左右，对于超出边界的邻节点，我们可以先不管它
是不是超出了范围，先往前走一步再说，如果发现走出界了再返回，这样也跟二叉树的结构对应了起来。
二叉树遍历就是先调用递归，然后发现了 root == None 再返回。

网格类型的问题和二叉树不同，在深度优先搜索中会出现重复的情况，我们需要添加避免重复的语句。

下面的是岛屿问题的框架
'''

# 网格 dfs 框架

# 判断 r，c 是不是在范围内
def inArea(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def dfs(grid, r, c):
    # 如果超出范围，则返回
    if not inArea(grid, r, c):
        return
    
    # 如果格子不是岛屿，直接返回
    elif grid[r][c] != 1:
        return
    
    # 最后，格子只能是岛屿了
    elif grid[r][c] == 1:
        # 把值变为 2，代表遍历过了
        grid[r][c] = 2
        
        dfs(grid, r-1, c)
        dfs(grid, r+1, c)
        dfs(grid, r, c-1)
        dfs(grid, r, c+1)

        return