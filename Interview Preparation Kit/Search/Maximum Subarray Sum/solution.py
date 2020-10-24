def solution(m, a):
    prefix = list()
    counter = 0
    for idx, num in enumerate(a):
        counter = (num + counter) % m
        prefix.append((counter, idx))

    prefix = sorted(prefix, key=lambda x: x[0])
    answer = prefix[-1][0]
    for idx in range(len(prefix) - 1):
        if prefix[idx][0] < prefix[idx+1][0]:
            if prefix[idx][1] > prefix[idx+1][1]:
                temp = (prefix[idx][0] - prefix[idx+1][0]) + m
                answer = max(answer, temp)
    return answer


if __name__ == "__main__":
    base_path = './Interview Preparation Kit/Search/Maximum Subarray Sum'
    input_filename = f'{base_path}/inputs/input.txt'
    output_filename = f'{base_path}/outputs/output.txt'

    f_in = open(input_filename, 'r')
    f_out = open(output_filename, 'r')

    T = int(f_in.readline())
    assert int(f_out.readline()) == T

    f_in.readline()
    f_out.readline()

    for t in range(T):
        n, m = map(int, f_in.readline().split())
        a = list(map(int, f_in.readline().strip().split()))

        my_answer = solution(m, a)
        answer = int(f_out.readline())

        assert my_answer == answer

        f_in.readline()
        f_out.readline()

    f_in.close()
    f_out.close()
