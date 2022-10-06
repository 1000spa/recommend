def 자카르유사도(A,B):
    A = set(A)
    B = set(B)
    return len(A&B)/len(A|B)

from itertools import combinations

items = [[1,2,3,4],[1,2,4,7],[1,2,8,7],[8,6,5,2]]
a = list(combinations(items,2))

print(a)

for i in a:
    유사도 = 자카르유사도(i[0],i[1])
    if 유사도 >= 0.5:
        print((i[0],i[1]),유사도)
        print(f"{a[a.index(i)][0]} 추천, {set(i[1]) - set(i[0])}")
        print(f"{a[a.index(i)][1]} 추천, {set(i[0]) - set(i[1])}")
