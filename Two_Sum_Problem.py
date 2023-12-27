class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and i != nums.index(diff):
                index_of_sum = nums.index(diff)
                my_list = [i,index_of_sum]
                print(my_list)
                return my_list
