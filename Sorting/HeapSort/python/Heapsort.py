"""
Heap Sort algorithm. Worst time : O(n * log(n))
"""

def heapify(a, count):
    start = int((count - 2) / 2)
    while start >= 0:
        traverse(a, start, count - 1)
        start -= 1

def traverse(a, start, end):
    root = start
    while (root * 2 + 1) <= end:
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child + 1) <= end and a[swap] < a[child + 1]:
            swap = child + 1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else:
            return

def heapsort(a):
    heapify(a, len(a))
    end = len(a) - 1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        end -= 1
        traverse(a, 0, end)
