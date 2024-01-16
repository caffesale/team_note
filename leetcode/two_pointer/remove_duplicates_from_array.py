class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      # iterate하는 pointer와 unique number를 탐색하는 포인터를 이용
      # 배열의 첫번째 요소는 항상 unique하므로 unique pointer == 1
      # iterate pointer는 배열 범위를 벗어나지 않기 위해 1부터
      j = 1
      for i in range(1, len(nums)):
        # unique number를 발견한 경우, iterator에 unique number를 삽입
        if nums[i] != nums[i -1]:
          nums[j] = nums[i]
          j += 1
      return j