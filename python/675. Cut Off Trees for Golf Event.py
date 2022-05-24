from typing import List
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        def bfs(sx,sy,i,j):
            m,n = len(forest), len(forest[0])
            visted = []
            q = deque([(0,sx,sy)])
            while q:
                d,i_,j_ = q.popleft()
                if i_ == i and j_ == j:
                    return d
                for (x,y) in [(i_+1, j_),(i_-1, j_),(i_, j_+1),(i_, j_-1)]:
                    if 0 <= x <= m  and 0 <= y <= n and (x,y) not in visted and  forest[x][y]:
                        visted.append((x,y))
                        d+=1
                        q.append((d,x,y))



        # sorted tress
        trees = sorted((h,i,j)for i,row in enumerate(forest) for h,j in enumerate(row))
        sx= sy= d =0
        for _ ,i,j in trees:
            d = bfs(sx,sy,i,j)
            if  d<0:
                return -1 #
            d +=d
            sx,sy = i,j
        return d
if __name__ == '__main__':
    forest =[[1,2,3],[0,0,4],[7,6,5]]
    ret = Solution().cutOffTree(forest)
    print(ret)


