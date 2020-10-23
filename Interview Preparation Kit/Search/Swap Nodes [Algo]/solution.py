class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        left_data = self.left.data if self.left else None
        right_data = self.right.data if self.right else None
        message = f'Node {self.data} -> {left_data}\t{right_data}'
        return message


if __name__ == "__main__":
    input_filename = \
        './Interview Preparation Kit/Search/Swap Nodes [Algo]/inputs/input.txt'
    output_filename = '../outputs/output.txt'

    f_in = open(input_filename, 'r')
    T = int(f_in.readline())
    f_in.readline()
    for t in range(T):
        print()
        N = int(f_in.readline())
        tree = {node: Node(node) for node in range(1, N+1)}

        for n in range(1, N+1):
            l, r = map(int, f_in.readline().split())
            if l in tree.keys():
                node = tree[n]
                node.left = tree[l]

            if r in tree.keys():
                node = tree[n]
                node.right = tree[r]

        for k, v in tree.items():
            print(v)

        L = int(f_in.readline())
        for _ in range(L):
            f_in.readline()
        f_in.readline()

    f_in.close()
