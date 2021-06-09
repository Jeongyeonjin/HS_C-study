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



list= [3,4,5,6,7,8,9]
target_number = 15
main(list, target_number)



