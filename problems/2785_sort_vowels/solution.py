class Solution(object):
    
    def sortVowels(self, s):
        string = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        string_vowels = []
        result = list(s)
        vowels_order = []

        for i in range(0, len(string)):
            if string[i].lower() in vowels:
                string_vowels.append({
                    'char': string[i],
                    'index': i,
                    'ascii': ord(string[i])
                })
                vowels_order.append(i)
            string_vowels = sorted(string_vowels, key=lambda k: k['ascii'])

        for i in range(0, len(string_vowels)):
            result[vowels_order[i]] = string_vowels[i]['char']
        
        return ''.join(result)
        
solution = Solution()
print(solution.sortVowels("Alphabet"))     

        