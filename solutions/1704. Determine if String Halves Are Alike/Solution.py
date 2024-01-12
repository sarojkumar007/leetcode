class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def isVowel(c: str):
            if c.lower() in ['a','e','i','o','u']:
                return True
            return False
        
        mid = int(len(s)/2)

        return len([c for c in s[:mid] if isVowel(c)]) == len([c for c in s[mid:] if isVowel(c)])