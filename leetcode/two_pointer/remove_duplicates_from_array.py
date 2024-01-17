class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      # iterate하는 pointer와 unique number를 탐색하는 포인터를 이용
      # 배열의 첫번째 요소는 항상 unique하므로 unique pointer == 1
      # iterate pointer는 배열 범위를 벗어나지 않기 위해 1부터
      unique_pointer = 1
      for i in range(1, len(nums)):
          if nums[i] != nums[i - 1]:
            nums[unique_pointer] = nums[i]
            unique_pointer += 1
      return unique_pointer