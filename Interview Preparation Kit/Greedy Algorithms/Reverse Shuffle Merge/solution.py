from collections import defaultdict
from collections import deque


def solution(s):
    alphabet_counter = defaultdict(int)
    for ch in s:
        alphabet_counter[ch] += 1

    required_counter = {k: v//2 for k, v in alphabet_counter.items()}

    s_reversed = s[::-1]
    answer = deque([])

    for ch in s_reversed:
        alphabet_counter[ch] -= 1
        if not required_counter[ch]:
            continue

        while answer and answer[-1] > ch:
            top = answer[-1]
            if alphabet_counter[top] >= required_counter[top] + 1:
                required_counter[top] += 1
                answer.pop()
            else:
                break
        answer.append(ch)
        required_counter[ch] -= 1

    return ''.join(answer)


if __name__ == "__main__":
    directory_name =\
        './Interview Preparation Kit/Greedy Algorithms/Reverse Shuffle Merge'
    input_filename = f'{directory_name}/inputs/input.txt'
    output_filename = f'{directory_name}/outputs/output.txt'

    f_in = open(input_filename, 'r')
    f_out = open(output_filename, 'r')

    T = int(f_in.readline())
    assert T == int(f_out.readline())

    f_in.readline()
    f_out.readline()
    for t in range(T):
        s = f_in.readline().strip()
        answer = f_out.readline().strip()

        my_answer = solution(s)
        assert my_answer == answer

        f_in.readline()
        f_out.readline()
    f_in.close()
    f_out.close()
