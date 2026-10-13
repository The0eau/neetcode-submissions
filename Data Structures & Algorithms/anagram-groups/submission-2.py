class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes = defaultdict(list)

        for s in strs:
            compte = [0] * 26
            for char in s:
                compte[ord(char) - ord("a")] += 1
            cle = tuple(compte)
            groupes[cle].append(s)

        return list(groupes.values())
            