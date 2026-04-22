class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = set()
        for string in strs:
            ana.add(''.join(sorted(string)))

        ana_list = list(ana)

        ana_groups = []

        for string in ana_list:
            ana_groups.append([s for s in strs if ''.join(sorted(s)) == string])

        return ana_groups