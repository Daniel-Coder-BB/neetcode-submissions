class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_s = {}
        string_t = {}
        for letter in s:
            if string_s.get(letter) is None:
                string_s[letter] = 1
            else:    
                string_s[letter] += 1

        for letter in t:
            if string_t.get(letter) is None:
                string_t[letter] = 1
            else:    
                string_t[letter] += 1 
        return string_t == string_s                        

           


        