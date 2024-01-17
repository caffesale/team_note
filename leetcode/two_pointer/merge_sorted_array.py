class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # in-place로 풀어야 하므로 two pointer를 사용한다.
    # 3개의 포인터를 사용하여 배열의 뒤에서부터 값을 채워나간다.
    i,j,k = m-1,n-1,m+n-1
    while j >= 0:
      if i >= 0 and nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
      else:
        nums1[k] = nums2[j]
        j -= 1
      k -= 1