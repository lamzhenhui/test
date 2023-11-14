# 1.合并两个有序的数组，数组都是非递减的，合井后的数组依然有序
# 要求： 需考志输入合法性，时间和空间复杂度。注意：可以用标准库啊数，或者自己知道的常用库西数操作,如果不记得,需要自己写原始代码实现。但星必须
# 保证是可以运行的
class Solution1:
    def merge(self, nums1, m, nums2, n):
        """
                # type nums1: List[int]
        # type m: int :type nums2: List[int]
        # type n: int
        # irtype: void Do not return anything, modify nums1 in-place instead.
        """

        index1 = 0
        index2 = 0
        ret = list()
        """
        两个数组的指针， 如果每次两个指针的指向的元素比较， 如果小的，就加入队列，然后指针加一，否则指针待定不加1
        """
        while index1 < m and index2 < n:

            while not nums1[index1]:
                index1 += 1
            compare_a = nums1[index1]
            while not nums2[index2]:
                index2 += 1
            compare_b = nums2[index2]

            if compare_a == compare_b:
                index1 += 1
                index2 += 1
                ret.extend([compare_a, compare_a])

            if compare_a < compare_b:
                ret.append(compare_a)
                index1 += 1
            elif compare_a > compare_b:
                ret.append(compare_b)
                index2 += 1
        # 兼顾到如果其中一组数组已经遍历完毕的情况
        if index1 < m:
            ret.extend([item for item in nums1[index1:] if item != 0])
        if index2 < n:
            ret.extend([item for item in nums2[index2:]if item != 0])
        return ret


"""
2.求n阶乘结果未尾连续0的个数，如5 ！=120，0的个数为 1"""


class Solution2:
    def trailingZeroes(self, n):
        """type n: int irtype: int"""
        # 主要是看【1，n】 中有多少个10  【1，2，。。。5.。。10.。。100】
        # 最大5的话， 那么就是 一个0；  如果10 因为前面还有5，所以这里是00，
        """
        5: 1 5//5 = 1
        10: 2  10 % 5 = 0  10 //5 = 2
        20: 4   0  4 
        100: ?  0  6?
        """

        target = 0

        for item in range(5, n+1, 5):
            while item % 5 == 0:
                while item // 5 > 0:
                    item = item // 5
                    target += 1
        return target


"""3.反转数字
反转数字，例子：
输入123，输出 321 ;输入-123，输出-321 ；输入 1032100，输出： 12301

"""


class Solution3:
    def reverse(self, x):
        pass


"""
4.（弃）求股票最大收益，给出一个数组，每个元素代表股票价格。设计一个算法，你可以多次买入和多次卖出，使得你的收益最大。算出最大收益。
"""
class Solution4:
    def maxProfit(self, prices):
        pass

if __name__ == "__main__":

    # s = Solution1()
    # nums1 = [1, 2, 3, 0]
    # nums2 = [2, 3, 4, 5]
    # ret = s.merge(nums1, len(nums1), nums2, len(nums2))
    # print(ret)

    # s2 = Solution2()
    # n = 100
    # ret = s2.trailingZeroes(n)
    # print(ret)

    s2 = Solution3()
    n = 323
    ret = s2.reverse(n)
    print(ret)
    s2 = Solution4()
    n = [12,13,35,32,25,63]
    ret = s2.maxProfit(n)
    print(ret)
