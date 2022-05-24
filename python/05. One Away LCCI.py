# coding=utf8


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m,n = len(first), len(second)
        if second> first:
            return self.oneEditAway(second,first)

        for i ,(x,y) in enumerate(zip(first,second)):
            if x != y:
                return first[i:]==second[i:m] if m ==n else first[i:] ==second[i:]
        return False








if __name__ == '__main__':
    first = "horse"
    second = "ros"
    # 输入
    # "horse"
    # "ros"
    # first = "pales"
    # second = "pal"
    ret = Solution().oneEditAway(first,second)
    print(ret)