from linkd_list.main import Node


class UnorderedList:
    def __init__(self):
        # 链表的入口
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        node = Node(item)
        # 链表中 在一个节点的基础上做修改， 首先将此系欸但的值保留，再将新的节点的next指向此节点
        node.set_next(self.head)
        self.head = node

    def __str__(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.get_data())
            current = current.get_next()
        return str(result)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item) -> bool:
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current.get_next() is not None:
            if item == current.get_data():
                break
            previous = current
            current = current.get_next()
        if current is None:
            raise "no such item in list"

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.add(31)
    my_list.add(77)
    print(my_list)
    print(my_list.size())
    print(my_list.search(109))
    print(my_list.search(77))
    print(my_list.remove(77))
    print(my_list)
    print(my_list.remove(31))
    print(my_list)
