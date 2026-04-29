class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char in '({[':
                stack.append(char)

            else:
                if len(stack)==0:
                    return False

                top_bracket=stack.pop()

                if char == ')' and top_bracket != '(':
                    return False
                elif char == '}' and top_bracket != '{':
                    return False
                elif char == ']' and top_bracket != '[':
                    return False

        
        return len(stack)==0

        