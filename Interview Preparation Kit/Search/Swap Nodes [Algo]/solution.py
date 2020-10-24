from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


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


def construct_tree(nodes):
    N = len(nodes)
    tree = {node: Node(node) for node in range(1, N+1)}
    levels = {1: 1}

    for n, (l, r) in enumerate(nodes):
        if l in tree.keys():
            node = tree[n+1]
            node.left = tree[l]
            levels[l] = levels[n+1] + 1

        if r in tree.keys():
            node = tree[n+1]
            node.right = tree[r]
            levels[r] = levels[n+1] + 1

    return tree, levels


def inorder_traverse(node, tree, orders):
    if node is None:
        return

    node_date = node.data

    inorder_traverse(tree[node_date].left, tree, orders)
    orders.append(node_date)
    inorder_traverse(tree[node_date].right, tree, orders)


def solution(nodes, commands):
    tree, levels = construct_tree(nodes)
    level2nodes = defaultdict(set)
    for k, v in levels.items():
        level2nodes[v].add(k)

    answer = list()
    max_level = max(level2nodes.keys())
    for command in commands:
        base = command
        while base <= max_level:
            for node in level2nodes[base]:
                tree[node].left, tree[node].right =\
                    tree[node].right, tree[node].left
            base += command

        inorders = list()
        inorder_traverse(tree[1], tree, inorders)
        answer.append(' '.join(map(str, inorders)))

    return answer


if __name__ == "__main__":
    base_directory =\
        './Interview Preparation Kit/Search/Swap Nodes [Algo]'
    input_filename = f'{base_directory}/inputs/input.txt'
    output_filename = f'{base_directory}/outputs/output.txt'

    f_in = open(input_filename, 'r')
    f_out = open(output_filename, 'r')
    T = int(f_in.readline())
    f_in.readline()
    f_out.readline()
    f_out.readline()

    for t in range(T):
        N = int(f_in.readline())
        tree = {node: Node(node) for node in range(1, N+1)}

        nodes = list()
        commands = list()

        for n in range(1, N+1):
            l, r = map(int, f_in.readline().split())
            nodes.append([l, r])

        C = int(f_in.readline())
        answer = list()
        for _ in range(C):
            command = int(f_in.readline())
            commands.append(command)
            answer.append(f_out.readline().strip())
        f_in.readline()
        f_out.readline()

        my_answer = solution(nodes, commands)

        assert my_answer == answer

    f_in.close()
    f_out.close()
