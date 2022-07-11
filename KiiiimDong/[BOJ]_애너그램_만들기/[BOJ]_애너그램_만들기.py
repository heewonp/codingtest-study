'''import sys
input = sys.stdin.readline

word = list(input().rstrip())
word2 = list(input().rstrip())
cnt = 0
cnt2 = 0
set1 = list(set(word))
set2 = list(set(word2))
for i in range(len(set1)):
    cnt += word2.count(set1[i])
for i in range(len(set2)):
    cnt2 += word.count(set2[i])
print((len(word)-cnt) + (len(word2)-cnt2))
'''
'''

from collections import Counter
a, b = Counter(input()), Counter(input())
print(sum((a-b).values()) + sum((b-a).values()))

print(a)
print(b)
print((a-b).values())
'''
word1_list = [0] * 26
word2_list = [0] * 26
word1 = input()
word2 = input()
for i in word1:
    word1_list[ord(i)-97] += 1
for j in word2:
    word2_list[ord(j)-97] += 1
cnt = 0
for i in range(26):
    if word1_list[i] or word2_list[i]:
        cnt += abs(word1_list[i]-word2_list[i])
print(cnt)

# ord(문자)
# 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
# ord('a')를 넣으면 정수 97을 반환합니다.

