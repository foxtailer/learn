class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    def containsDuplicate_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))<len(nums)

    def containsDuplicate_3(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp_dict = set()

        for item in nums:
            if item in temp_dict:
                return True
            else:
                temp_dict.add(item)
        return False

    def containsDuplicate_4(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp_dict = {}

        for item in nums:
            if temp_dict.get(item, 0):
                return True
            else:
                temp_dict[item] = 1
        return False    

s = Solution()

print(s.containsDuplicate([1,2,3]))
print(s.containsDuplicate([1,2,2,3]))
print('*')
print(s.containsDuplicate_2([1,2,3]))
print(s.containsDuplicate_2([1,2,2,3]))
print('*')
print(s.containsDuplicate_3([1,2,3]))
print(s.containsDuplicate_3([1,2,2,3]))
print('*')
print(s.containsDuplicate_4([1,2,3]))
print(s.containsDuplicate_4([1,2,2,3]))
