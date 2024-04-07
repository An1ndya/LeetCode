class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        FirstParenthesisStack = []
        AstericStack = []
        for i in range(n):
            if s[i] == '(':
                FirstParenthesisStack.append(i)
            elif  s[i] == '*':
                AstericStack.append(i)
            else:
                # ) parenthesis found,first check for available opening parenthesis (
                if FirstParenthesisStack:
                    FirstParenthesisStack.pop()
                elif AstericStack:
                    #no opening parenthesis, use asteric
                    AstericStack.pop()
                else:
                    #left with only closing parenthesis, so no valid parenthesis
                    return False
        #we need to check if remaining ( and * create valid parenthesis
        while FirstParenthesisStack and AstericStack:
            # *(... this positioning lead to invalid parenthesis, as last one is opening one
            if FirstParenthesisStack.pop() > AstericStack.pop():
                #opening ( is after *, so (( or )( can be form both invalid
                return False
        #one of them must be empty ...remaining asteric can be empty
        #if first parenthesis is empty means valid, else non matching ( create invalid
        return not FirstParenthesisStack
                