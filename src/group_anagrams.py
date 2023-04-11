from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_me_dict: dict[str, List[str]] = {}
        for word in strs:
            temp = str(sorted(word))
            if temp in return_me_dict:
                return_me_dict[temp].append(word)
            else:
                return_me_dict[temp] = [word]
        print(return_me_dict)
        return list(return_me_dict.values())
