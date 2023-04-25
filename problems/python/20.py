'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # iterating over each character in the input string s
        for char in s:
            # If the character is an opening parenthesis, brace, or bracket, it is added to a stack
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            # If the character is a closing parenthesis, brace, or bracket
            else:
                # it is checked if it pairs with the last character added to the stack. If a matching pair is found, the last character is removed from the stack.
                if not stack:
                    return False
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack