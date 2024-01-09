class Dequeue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        if self.is_empty():
            raise Exception("Dequeue is empty")
        return self.items.pop()

    def remove_rear(self):
        if self.is_empty():
            raise Exception("Dequeue is empty")
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def pal_checker(a_string) -> bool:
    char_dequeue = Dequeue()
    for ch in a_string:
        char_dequeue.add_front(ch)

    while char_dequeue.size() > 1:
        first = char_dequeue.remove_front()
        last = char_dequeue.remove_rear()
        if first != last:
            return False
    return True


if __name__ == "__main__":
    print(pal_checker("toot"))
    print(pal_checker("lsdkjfskf"))
