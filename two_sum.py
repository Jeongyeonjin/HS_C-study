class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.list = nums
        self.target_number = target

        for i in range(0, len(self.list)):
            i_index = i

            for j in range(i + 1, len(self.list)):

                num = self.list[i] + self.list[j]
                if self.target_number == num:
                    return i, j




