lit = [10, 25, 30]
iterL = filter(none, lst)
for i in iterL:
    print(i)

#함숮정의
def getBiggerThan20(i):
    return i >20

print("----필터링 함수 사용------")
iterL =  filter(getBiggerThan20, lst)
for i in iterL:
    print(i)
