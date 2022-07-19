# [CFS] A. Another String Minimization Problem

문제 링크 : https://codeforces.com/contest/1706/problem/A

-------------------------
## 문제 요약
  - B m개로 이루어진 문자열 s를 규칙에 따라 변경할 때, 사전 순으로 가장 먼저 오는 문자열을 구하는 문제
  - a 수열에서의 i번째 요소에 대해 s의 ai번째나 (m+1-ai)번째 위치의 문자를 'A'로 변경하는 작업을 진행한다.

## 접근 방식
  - ai와 (m+1-ai) 중 더 앞쪽에 있는 문자가 'B'라면 이를 'A'로 변경, 아니면 뒤쪽의 문자를 'A'로 변경
