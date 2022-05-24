from typing import List
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        def bfs(sx,sy,i,j):
            m,n = len(forest), len(forest[0])
            visted = {(sx,sy)}
            q = deque([(0,sx,sy)])
            while q:
                d,i_,j_ = q.popleft()
                if i_ == i and j_ == j:
                    return d
                for (x,y) in [(i_+1, j_),(i_-1, j_),(i_, j_+1),(i_, j_-1)]:
                    if 0 <= x < m  and 0 <= y < n and (x,y) not in visted and  forest[x][y]:
                        visted.add((x,y))
                        if x == i and y == j:
                            return d + 1

                        q.append((d+1,x,y))
            return -1



        # sorted tress
        trees = sorted((h,i,j)for i,row in enumerate(forest) for j,h in enumerate(row) if h >0)
        sx= sy= d =0
        for _ ,i,j in trees:
            d_ = bfs(sx,sy,i,j)
            if  d_<0:
                return -1 #
            d +=d_
            sx,sy = i,j
        return d
if __name__ == '__main__':
    forest =[[4,2,3],[0,0,1],[7,6,5]]
    ret = Solution().cutOffTree(forest)
    print(ret)
    """
    输入：
[[4,2,3],[0,0,1],[7,6,5]]
输出：
14
预期结果：
10"""


