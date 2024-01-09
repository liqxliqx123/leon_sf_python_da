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


# if __name__ == "__main__":
#     print(par_checker("((()))"))
#     print(par_checker("((())"))
#
#     print(balance_checker("((]]]"))
#     print(balance_checker("({]]]"))
#     print(balance_checker("({[]]"))
#     print(balance_checker("({[]}"))
#     print(balance_checker("({[]})"))


#  十进制转换为二进制
#  除2取余法
def divide_by_2(dec_number) -> str:
    s = Stack()
    while dec_number > 0:
        rem = dec_number % 2
        s.push(rem)
        dec_number = dec_number // 2
    bin_string = ""
    while not s.is_empty():
        bin_string += str(s.pop())
    return bin_string


# 十进制转换为任意进制
def base_converter(dec_number, base) -> str:
    digits = "0123456789ABCDEF"
    s = Stack()
    while dec_number > 0:
        rem = dec_number % base
        s.push(rem)
        dec_number = dec_number // base
    new_string = ""
    while not s.is_empty():
        new_string += digits[s.pop()]
    return new_string


# if __name__ == "__main__":
#     print(base_converter(25, 2))
#     print(base_converter(25, 8))
#     print(base_converter(25, 10))
#     print(base_converter(14, 16))


# 中序表达式转换为后续表达式
def infix_to_postfix(infix_expr) -> str:
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    s = Stack()
    postfix_list = []
    token_list = infix_expr.split()
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            s.push(token)
        elif token == ")":
            top_token = s.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = s.pop()
        else:
            while not s.is_empty() and prec[s.peek()] >= prec[token]:
                postfix_list.append(s.pop())
            s.push(token)
    while not s.is_empty():
        postfix_list.append(s.pop())
    return " ".join(postfix_list)


# if __name__ == "__main__":
#     print(infix_to_postfix("A * B + C * D"))


# 后续表达式求值
def postfix_eval(postfix_expr) -> int:
    s = Stack()
    token_list = postfix_expr.split()
    for token in token_list:
        if token in "0123456789":
            s.push(int(token))
        else:
            op2 = s.pop()
            op1 = s.pop()
            result = do_math(token, op1, op2)
            s.push(result)
    return s.pop()


def do_math(op, op1, op2) -> int:
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 // op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2


# if __name__ == "__main__":
#     print(postfix_eval("7 8 + 3 2 + /"))
