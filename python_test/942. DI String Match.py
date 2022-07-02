# -*- coding:utf-8 -*-
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        i_index = 0
        d_index = n = len(s)
        ret = ["" for item in range(n + 1)]


        for index, item in enumerate(s):
            print(index)
            if item == "I":
                ret[index] = i_index
                i_index += 1

            if item == "D":
                ret[index] = d_index
                d_index -= 1
        ret[n] = index
        return ret
if __name__ == '__main__':
    s = "IID"
    ret = Solution().diStringMatch(s)
    print(ret)