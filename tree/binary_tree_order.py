from tree.binary_tree import BinaryTree
import operator

# 树的前中后序遍历
# 前序遍历：根节点->左子树->右子树
# 中序遍历：左子树->根节点->右子树
# 后序遍历：左子树->右子树->根节点

# 树的遍历使用递归实现， 逻辑上比较简单

def pre_order(root):
    """前序遍历"""
    if root is None:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    """中序遍历"""
    if root is None:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)


def post_order(root):
    """后序遍历"""
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val)


# 后序求值函数
def postorderval(tree):
    operatosrs = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    ret1 = None
    ret2 = None
    if tree:
        ret1 = postorderval(tree.left_child)
        ret2 = postorderval(tree.right_child)
        if ret1 and ret2:
            return operatosrs[tree.root](ret1, ret2)
        else:
            return tree.root
    else:
        return None


# 中序遍历函数  还原完全括号表达式
def print_exp(tree):
    ret = ""
    if tree:
        ret = '(' + print_exp(tree.left_child)
        ret = ret + str(tree.root)
        ret = ret + print_exp(tree.right_child) + ')'
    return ret


if __name__ == "__main__":
    x = BinaryTree('*')
    x.insert_left('+')
    l = x.get_left_child()
    l.insert_left(4)
    l.insert_right(5)
    x.insert_right(7)
    print(print_exp(x))
    print(postorderval(x))
