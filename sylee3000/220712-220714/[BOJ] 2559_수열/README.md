# [BOJ] 2559_수열

문제 링크 : https://www.acmicpc.net/problem/2559

---------------
## 문제 요약
  - N일 간의 온도가 주어질 때, 연속된 K일동안의 온도의 합이 가장 큰 값을 출력하는 문제

## 접근 방식
  - N일 간의 온도를 deque인 temp로 저장
  - 1일차부터 temp에서 popleft로 온도를 하나씩 빼주면서 temp_part에 더해준 뒤 deque인 temp_left에 추가
  - 6일차부터 temp_left에서 popleft로 온도를 하나씩 빼서 temp_part에 빼준다.
  - temp_part가 max_res(기본값 : -1000000000)보다 크면 max_res에 temp_part를 저장
