class Solution(object):

    def __init__(self):
        self.timer = 0
        self.char_index = 0
        self.alphabet = list('abcdefghijklmnopqrstuvwxyz')
    
    def reset(self):
        self.timer = 0
        self.char_index = 0

    def find_next_char(self, char):
        if self.alphabet[self.char_index] == char:
            self.timer += 1
            return
        else:
            dest_index = self.alphabet.index(char)
            self.timer += abs(self.char_index - dest_index)
            self.char_index = dest_index
            self.timer += 1

    def minTimeToType(self, word):
        for char in word:
            self.find_next_char(char)
        result = self.timer
        self.reset()
        return result
solution = Solution()
print(solution.minTimeToType('bza'))
