from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana=defaultdict(list)
        res=[]
        for s in strs:
            s_sort=tuple(sorted(s))
            ana[s_sort].append(s)
        for r in ana.values():
            res.append(r)
        return res

            