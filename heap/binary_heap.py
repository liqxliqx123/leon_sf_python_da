class BinaryHeap:
    def __init__(self):
        self._heap = []

    def insert(self, item):
        self._heap.append(item)
        self._percolate_up(len(self._heap) - 1)

    # 保证二叉堆的有序性; 比较插入的值和其父节点， 如果小于父节点， 则交换位置
    def _percolate_up(self, i):
        while (i - 1) // 2 >= 0:
            parent = (i - 1) // 2
            if self._heap[i] < self._heap[parent]:
                self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
            else:  # parent is smaller than child
                break
            i = parent

    def delete(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        self._percolate_down(0)
        value = self._heap.pop()
        return value

    def _percolate_down(self, i):
        # 元素和其较小的子节点比较， 如果大于子节点， 则交换位置
        while i * 2 + 1 < len(self._heap):
            sm_child = self._get_min_child(i)
            if self._heap[i] > self._heap[sm_child]:
                self._heap[i], self._heap[sm_child] = self._heap[sm_child], self._heap[i]
            else:
                break
            i = sm_child

    def _get_min_child(self, i):
        if 2 * i + 1 == len(self._heap) - 1:
            return 2 * i + 1
        if self._heap[2 * i + 1] <= self._heap[2 * i + 2]:
            return 2 * i + 1
        else:
            return 2 * i + 2

    def heapify(self, not_a_heap):
        self._heap = not_a_heap[:]
        # 中位数 中位数yixia
        i = len(self._heap) // 2 - 1
        while i >= 0:
            self._percolate_down(i)
            i -= 1


if __name__ == "__main__":
    heap = BinaryHeap()
    heap.heapify([9, 6, 5, 2 ,3, 1, 8, 4, 10])
    print(heap._heap)

