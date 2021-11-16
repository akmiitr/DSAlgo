'''
This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
'''


def can_pop(opening_bracket, closing_bracket):
    if opening_bracket == "{" and closing_bracket == "}":
        return True
    if opening_bracket == "[" and closing_bracket == "]":
        return True
    if opening_bracket == "(" and closing_bracket == ")":
        return True
    return False


def balance(expression):
    stack = []
    for s in expression:
        if stack and can_pop(stack[len(stack) - 1], s):
            stack.pop()
        else:
            stack.append(s)
    if not stack:
        print("Parenthesis are balanced")
        return False
    print("Parenthesis are not balanced")
    return False


if __name__ == '__main__':
    balance("([])[]({})")
    balance("((()")
    balance("([)]")
