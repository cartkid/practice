class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
        # Each letter in magazine can only be used once in ransomNote.

        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, "", 1)
            else:
                return False

        return True
