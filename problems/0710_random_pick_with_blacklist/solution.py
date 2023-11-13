import random

#Attempt 1 using lists
# Not Expected. Exceeds Memory Limit. Would likely need to use a hashmap or dict. 
class Solution(object):

    def __init__(self, n, blacklist):
        self.n = n
        self.blacklist = blacklist

        self.valid_numbers = list(range(0, self.n))
        for num in self.blacklist:
            self.valid_numbers.remove(num)
        self.n = len(self.valid_numbers)
    
    def pick(self):
        return self.valid_numbers[random.randint(0, self.n-1)]

solution = Solution(30, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(solution.pick())