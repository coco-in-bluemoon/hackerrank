def solution(k, arr):
    arr_set = set(arr)
    counter = 0
    for src in arr_set:
        dst = src + k

        counter += (src != dst and dst in arr_set)
    return counter


if __name__ == "__main__":
    base_path = './Interview Preparation Kit/Search/Pairs'
    input_filename = f'{base_path}/inputs/input.txt'
    output_filename = f'{base_path}/outputs/output.txt'

    f_in = open(input_filename, 'r')
    f_out = open(output_filename, 'r')

    T = int(f_in.readline())
    assert int(f_out.readline()) == T

    f_in.readline()
    f_out.readline()

    for t in range(T):
        n, k = map(int, f_in.readline().split())
        arr = [0] * n
        for idx, num in enumerate(f_in.readline().split()):
            arr[idx] = int(num)

        my_answer = solution(k, arr)
        answer = int(f_out.readline())

        assert my_answer == answer

        f_in.readline()
        f_out.readline()

    f_in.close()
    f_out.close()