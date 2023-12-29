import operator

from tree.binary_tree import BinaryTree
from stack.main import Stack


# 二叉树的应用：解析树
def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    e_tree = BinaryTree('')
    p_stack = Stack()
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i.isdigit():
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree


def evaluate(parse_tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()
    if left_child and right_child:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.get_root_val()


if __name__ == "__main__":
    t = build_parse_tree("( 3 + ( 4 * 5 ) )")
    print(t.get_root_val())
    print(t.get_left_child().get_root_val())
    print(t.get_right_child().get_root_val())
    print(t.get_right_child().get_left_child().get_root_val())
    print(t.get_right_child().get_right_child().get_root_val())
    print(evaluate(t))
