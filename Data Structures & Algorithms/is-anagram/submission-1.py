class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_table = self.build_table(s)
        t_table = self.build_table(t)
        
        if len(s_table.keys()) != len(t_table.keys()):
            return False

        for item in s_table:
            try:
                if s_table[item] != t_table[item]:
                    return False
            except KeyError:
                return False

        return True

    def build_table(self, m: str):
        table = {}

        for letter in m:
            if table.get(letter) is not None:
                table[letter] += 1
            else:
                table[letter] = 1

        return table
