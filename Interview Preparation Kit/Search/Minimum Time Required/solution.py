def calculate_workload(time, machines):
    return sum([time // m for m in machines])


def solution(goal, machines):
    left = 1
    right = goal * min(machines)

    while left < right:
        middle = (left + right) // 2

        workload = calculate_workload(middle, machines)
        if workload < goal:
            left = middle + 1
        else:
            right = middle

    return right


if __name__ == "__main__":
    base_path = './Interview Preparation Kit/Search/Minimum Time Required'
    input_filename = f'{base_path}/inputs/input.txt'
    output_filename = f'{base_path}/outputs/output.txt'

    f_in = open(input_filename, 'r')
    f_out = open(output_filename, 'r')

    T = int(f_in.readline())
    assert int(f_out.readline()) == T

    f_in.readline()
    f_out.readline()

    for t in range(T):
        n, goal = map(int, f_in.readline().split())
        machines = list(map(int, f_in.readline().strip().split()))

        my_answer = solution(goal, machines)
        answer = int(f_out.readline())

        assert my_answer == answer

        f_in.readline()
        f_out.readline()

    f_in.close()
    f_out.close()
