class Solution:
    def sortArray(self, nums):
        self.merge_sort(nums, 0, len(nums)-1)
        return nums

    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l+r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid+1, r)
        i, j = l, mid+1
        tmp = []
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                # 这里nums[j]< nums[i]可达到一样效果
                #
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1

        nums[l:r+1] = tmp


if __name__ == "__main__":
    print(Solution().sortArray(nums=[1, 9, 2, 4]))
