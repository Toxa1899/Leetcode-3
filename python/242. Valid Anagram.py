class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict : int = {}
        t_dict : int = {}

        for char_s , char_t in zip(s, t):
            s_dict[char_s] = s_dict.get(char_s, 0) + 1
            t_dict[char_t] = t_dict.get(char_t, 0) + 1
        
        return s_dict == t_dict