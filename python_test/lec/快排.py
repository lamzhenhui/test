import random


class Solution(object):
    def sortArray(self, nums):
        self.quick_sort(nums, 0, len(nums)-1)
        return nums

    def quick_sort(self, nums, l, r):
        if l < r:
            p = self.find_pivot(nums, l, r)
            # if p == 0:
            #     self.quick_sort(nums, l, r)
            self.quick_sort(nums, l, p-1)
            self.quick_sort(nums, p+1, r)  # 这里需要注意右边的边界不能是len(nums）

    def find_pivot(self, nums, l, r):

        i = random.randint(
            range(len(nums))[l], range(len(nums))[r])
        self.swap(nums, i, r)
        q = nums[r]
        index = l-1
        for p_index in range(l, r):
            if nums[p_index] <= q:  # 需要注意这里如果对比的数相同， 也需要往前边挪
                index += 1
                self.swap(nums, index, p_index)
        self.swap(nums, index+1, r)
        return index+1

    def swap(self, nums, i, r):
        right = nums[r]
        rang = nums[i]
        nums[r], nums[i] = rang, right


if __name__ == "__main__":
    # nums = [-3, 1, 2]
    nums = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
    # nums = [0, 0, 0]
    ret = Solution().sortArray(nums)
    print(ret)
