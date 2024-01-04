from stack.main import Stack


#  小括号匹配
def par_checker(symbol_string) -> bool:
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            # 压栈
            s.push(symbol)
        else:
            # )
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()


# 多种括号匹配
def balance_checker(symbol_string) -> bool:
    s = Stack()
    left = ["(", "{", "["]
    for symbol in symbol_string:
        if symbol in left:
            # 压栈
            s.push(symbol)
        else:
            # ) } ]
            if s.is_empty():
                return False
            lef = s.pop()
            if not matches(lef, symbol):
                return False
    return s.is_empty()


def matches(l, r: str) -> bool:
    left = ["(", "{", "["]
    right = [")", "}", "]"]
    return left.index(l) == right.index(r)


if __name__ == "__main__":
    print(par_checker("((()))"))
    print(par_checker("((())"))

    print(balance_checker("((]]]"))
    print(balance_checker("({]]]"))
    print(balance_checker("({[]]"))
    print(balance_checker("({[]}"))
    print(balance_checker("({[]})"))
