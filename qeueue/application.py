from qeueue.main import Queue


# 传土豆模拟程序
def hot_potato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()


# if __name__ == "__main__":
#     print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
