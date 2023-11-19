class TwoNumbersProduct:
    def find_two_numbers_with_product(self, nums, target):
        num_index_map = {}

        for index, num in enumerate(nums):
            if num == 0 and target == 0:
                if nums.count(0) > 1:
                    return [index for index, n in enumerate(nums) if n == 0][:2]
            elif target % num == 0:
                complement = target // num
                if complement in num_index_map:
                    return [num_index_map[complement], index]
            num_index_map