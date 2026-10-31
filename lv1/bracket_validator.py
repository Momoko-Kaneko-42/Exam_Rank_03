def bracket_validator(s: str) -> bool:
    pairs ={
        ")":"(",
        "]":"[",
        "}":"{",
    }

    stack = []

    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in pairs:
            if not stack:
                return False
            last: str = stack.pop()
            if last != pairs[c]:
                return False
#       elif c in pairs and (not stack or stack.pop() != pairs[c]):
#           return False
    if not stack:
        return True
    else:
        return False
#   return not stack

def main() -> None:
    print(bracket_validator("([])"))
    print(bracket_validator("([)]"))
    print(bracket_validator("(()"))
    print(bracket_validator(""))
    print(bracket_validator("hello(world)"))

if __name__=="__main__":
    main()