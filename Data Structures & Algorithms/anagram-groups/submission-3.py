class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes = defaultdict(list)

        for s in strs:
            cle = "".join(sorted(s))
            groupes[cle].append(s)
        return list(groupes.values())
            