def 자카르유사도(A,B):                     # 유사도 계산하는 함수
    A = set(A)
    B = set(B)
    return len(A&B)/len(A|B)

with open('items.txt','r',encoding='utf-8') as file_data:
    lines = file_data.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
        

유저_데이터 = []

for i in lines:
    유저_데이터.append(list(i.split(',')))

def 추천(m:str):                    # 유사도(1 : 일치, 0 : 완전히 다름, 0.5 : 절반이 같음)가 0.5 이상인 유저 데이터에서 추천 대상자가 플레이하지 않는 게임을 반환하는 함수
    global 유저_데이터
    main = list(m.split(','))
    items = 유저_데이터
    추천 = []
    for i in items:
        a = set(i)
        b = set(main)
        유사도 = 자카르유사도(a,b)
        if 유사도 >= 0.5:
            추천.append(a-b)
    return 추천