class Solution(object):
    def divisorSubstrings(self, num, k):
        num = str(num)
        valid_count = 0
        for i in range(len(num)-k+1):
            sub = num[i:i+k]
            if int(sub) != 0:
                if int(num) % int(sub) == 0:
                    valid_count += 1
        return valid_count

solution = Solution()
print(solution.divisorSubstrings(120120, 2))