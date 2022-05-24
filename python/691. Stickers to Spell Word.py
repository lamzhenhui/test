# class Solution:
#     count_num = 0
#
#     def minStickers(self, stickers: List[str], target: str) -> int:
#         target_lst = list(set([item for item in target]))
#         stickers = [set(item) for item in stickers]
#
#         print(target)
#         new_stickers = list()
#         find_info = dict()
#         not_find = dict()
#         for index, item in enumerate(stickers):
#             nex_lst = list()
#             for it in item:
#                 if not not_find.get(index) and not_find.get(index) != "":
#                     not_find[index] = []
#                 if not find_info.get(index) and find_info.get(index) != "":
#                     find_info[index] = 0
#
#                 if it in target_lst:
#                     find_info[index] += 1
#
#                 else:
#                     not_find[index].append(it)
#             print(find_info, not_find)
#         max_ind = max(list(find_info.values()))
#         print(88, max_ind)
#         print(99, stickers[max_ind], not_find[max_ind])
#         this_find = list(set([item for item in stickers[max_ind] if item not in not_find[max_ind]]))
#
#         nex_target = []
#         for item in target:
#             if item not in this_find:
#                 nex_target.append(item)
#         nex_t = "".join(nex_target)
#
#         nex_s = [str(value) for item, value in not_find.items() if value]
#         if this_find:
#             print("this_find %s" % this_find)
#             self.count_num += 1
#             return self.minStickers(nex_t, nex_s)
#             print(">>")
#         else:
#             return self.count_num
from collections import Counter
from typing import List
from functools import cache
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)
        @cache
        def func(march):
            if not march:
                return 0
            ret = m +1
            for sticker in stickers:
                left = march
                c = Counter(sticker)
                for index, item in enumerate(target):
                    if c[item] and march >> index & 1:
                        c[item] -=1
                        left ^= 1 << index
                    if left < march:
                        ret =  min(ret, func(left)+1)
                    print(ret)
            return ret
        ret = func((1<<m)-1)

        return ret if ret <= m else -1

if __name__ == '__main__':
    stickers = ["with", "example", "science"]
    target = "thehat"
    ret = Solution().minStickers(stickers,target)
    print(999,ret)


