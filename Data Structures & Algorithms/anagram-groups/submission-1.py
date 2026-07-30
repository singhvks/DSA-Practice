class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique_list = {k for k in set(["".join(sorted(i)) for i in strs])}
        output = []

        for k in unique_list:
            output.append([i for i in strs if ''.join(sorted(i)) == k])
            
        return output
