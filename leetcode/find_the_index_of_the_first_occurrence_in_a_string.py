class Solution:
  def strStr(self, haystack, needle):
    # 1. Brute Force
    # Time: O(n^2)
    # Space: O(1)
    # if needle == "":
    #   return 0
    # for i in range(len(haystack)):
    #   slice_list= haystack[i:i+len(needle)]
    #   if needle == slice_list:
    #     return i
    # return -1
    
    # 2. KMP
    lps = [0] * len(needle)
    prefix = 0
    for i in range(1, len(needle)):
      while prefix > 0 and needle[i] != needle[prefix]:
        prefix = lps[prefix - 1]
      if needle[i] == needle[prefix]:
        prefix += 1
        lps[i] = prefix

    n = 0
    for h in range(len(haystack)):
      while n > 0 and haystack[h] != needle[n]:
        n = lps[n - 1]
      if needle[n] == haystack[h]:
        n += 1
      if n == len(needle):
        return h - n + 1
      
    return -1