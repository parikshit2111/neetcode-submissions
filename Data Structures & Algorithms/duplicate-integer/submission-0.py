from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num=sorted(nums)
        for i in range(0,len(num)-1):
            j=i+1
            if num[i]==num[j]:
                return True
        return False
            