import heapq

class Node: //Minheapnode
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class Huffman:
    def _print_codes(self, root, code):
        if root is None:
            return 
        if root.data != '$':
            print(f"{root.data}: {code}")
        self._print_codes(root.left, code + "0")
        self._print_codes(root.right, code + "1")

    def build(self, data, freq):
        min_heap = []
        for i in range(len(data)):
            heapq.heappush(min_heap, Node(data[i], freq[i]))

        while len(min_heap) > 1:
            left = heapq.heappop(min_heap)
            right = heapq.heappop(min_heap)
            temp = Node('$', left.freq + right.freq)
            temp.left = left
            temp.right = right
            heapq.heappush(min_heap, temp)

        self._print_codes(min_heap[0], "")

def main():
    data = ['A', 'B', 'C', 'D']
    freq = [23, 12, 34, 10]
    huffman = Huffman()
    huffman.build(data, freq)

if __name__ == "__main__":
    main()


