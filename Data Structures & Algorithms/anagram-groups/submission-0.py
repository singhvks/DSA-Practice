class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique_dict = {k:[] for k in set(["".join(sorted(i)) for i in strs])}
        output = []

        for k in unique_dict.keys():
            output.append([i for i in strs if ''.join(sorted(i)) == k])
            
        return output
