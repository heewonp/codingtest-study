S = input()
A = set()

for i in range(len(S)): #abcde 가 있으면 a,ab,abc,abcd,abcde출력
    for j in range(i,len(S)):
        N= S[i:j+1]
        #print(N)
        A.add(N)
#print(A) # 중복이 제거된채로 출력됨
print(len(A))