class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in strs:
            count = [0] * 26
            for char in i:
              count[ord(char) - ord('a')] += 1 

            key = tuple(count)

            if key in groups:
                groups[key].append(i)
            
            else:
                groups[key] = [i]

        return list(groups.values())

        