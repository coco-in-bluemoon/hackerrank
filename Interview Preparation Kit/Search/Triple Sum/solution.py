def solution(a, b, c):
    answer = 0
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    adx = 0
    cdx = 0
    for num in b:
        while adx < len(a) and a[adx] <= num:
            adx += 1
        while cdx < len(c) and c[cdx] <= num:
            cdx += 1

        answer += (adx * cdx)

    return answer


if __name__ == "__main__":
    base_directory =\
        './Interview Preparation Kit/Search/Triple Sum'
    input_filename = f'{base_directory}/inputs/input.txt'
    output_filename = f'{base_directory}/outputs/output.txt'

    f_in = open(input_filename, 'r')
    f_out = open(output_filename, 'r')
    T = int(f_in.readline())
    assert int(f_out.readline()) == T
    f_in.readline()
    f_out.readline()

    for t in range(T):
        lena, lenb, lenc = map(int, f_in.readline().split())

        arra = list(map(int, f_in.readline().rstrip().split()))
        arrb = list(map(int, f_in.readline().rstrip().split()))
        arrc = list(map(int, f_in.readline().rstrip().split()))

        answer = int(f_out.readline())

        my_answer = solution(arra, arrb, arrc)
        assert my_answer == answer

        f_in.readline()
        f_out.readline()

    f_in.close()
    f_out.close()
