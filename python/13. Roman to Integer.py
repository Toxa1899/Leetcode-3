from fontTools.subset import prune_hints


class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
          'M': 1000,
          'CM': 900,
          'D': 500,
          'CD': 400,
          'C': 100,
          'XC': 90,
          'L': 50,
          'XL': 40,
          'X': 10,
          'IX': 9,
          'V': 5,
          'IV': 4,
          'I': 1,
        }

        answer = 0  # результат сложения

        i = 0 # индекс

        while i < len(s):

            if i == len(s) - 1:
                answer += roman_numerals.get(s[i])
                i += 1

            else:
                if s[i:i+2] in roman_numerals:
                    answer += roman_numerals.get(s[i:i+2])
                    i += 2
                else:
                    answer += roman_numerals.get(s[i])
                    i += 1

        return  answer







s = Solution()
print(s.romanToInt("MCMXCIV"))
