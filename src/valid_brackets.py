class Solution:
    starting_brackets = ["(", "[", "{"]
    ending_brackets = [")", "]", "}"]

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in Solution.starting_brackets:
                stack.append(char)
            elif char in Solution.ending_brackets:
                if len(stack) == 0:
                    return False
                index = Solution.ending_brackets.index(char)
                if stack[-1] == Solution.starting_brackets[index]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
