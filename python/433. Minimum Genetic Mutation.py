# -*- coding:utf-8 -*-
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        dif_info = list()
        tag_bank = list()
        dif_index = list()

        for i, t in enumerate(start):
            if t != end[i]:
                dif_index.append(i)
                dif_info.append(t)

        for info in bank:
            data = ''
            for item in dif_index:
                data = "{}{}".format(data, info[item])
            tag_bank.append(str(data))

        print(dif_info)
        print(tag_bank)
        print(dif_index)
        # 轮询出所有的可能组合 可能的组合有len(dif_info) *2
        for item1 in dif_info:
            for item2 in dif_info:
                pass


if __name__ == '__main__':
    start, end, bank = "AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

    Solution().minMutation(start, end, bank)