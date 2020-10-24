# Interview Preparating Kit

## Greedy Algorithms
### [Reverse Shuffle Merge](./Interview%20Preparation%20Kit/Greedy%20Algorithms/Reverse%20Shuffle%20Merge/solution.py)
- 문자열 처리 문제
- 가장 앞선 사전순의 문자열을 찾기 위한 방법 고민
  - 문제 해결을 위해 문자를 순회하면서 해당 문자를 포함시킬지 말지 판단하는 것은 답이 아니다
  - 일단 추가 + 이후 기존의 것을 빼는 방법으로 탐색

## Search
### [Swap Nodes \[Algo\]](Interview%20Preparation%20Kit/Search/Swap%20Nodes%20[Algo]/solution.py)
- 트리 노드를 클래스로 구현해서 left child와 right child swap

### [Pairs](Interview%20Preparation%20Kit/Search/Pairs/solution.py)
- 시간 효율성을 위해서 집합(set) 활용

### [Triple Sum](Interview%20Preparation%20Kit/Search/Triple%20Sum/solution.py)
- 시간 효율성을 위해서 정렬된 집합(set) 활용

### [Minimum Time Required](./Search/Minimum%20Time%20Required/solution.py)
- BST

### [Maximum Subarray Sum](./Search/Maximum%20Subarray%20Sum/solution.py)
- Prefix 배열을 구해서 0~n 까지의 합을 미리 구한다 + 합을 기준으로 정렬까지
- 차이가 가장 큰 경우의 수를 최종 비교한다
  - prefix 배열 상에서 최대 값
  - 정렬된 prefix 배열 상에서 인접한 두 값의 차이로 음수가 만들어질 수 있는 경우