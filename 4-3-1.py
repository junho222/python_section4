#a = 'hello'
#print(type(a))
#print(a[0:3])
#print(a[-1:])


#for t in a :
    #print(type(t))

#리스트 자료형(순서o, 중복o, 수정o, 삭제o)

#선언
a = []
b = list()
c = [0,0,1,2]
d = [0,1,'car','apple','apart']
e = [0,1,['car','apple','apart']]

#인덱싱
print("#========#")
print('d -', type(d), d)
print('d -',  d[1])
print('d -',  d[0]+d[1]+d[1])
print('e -',  e[-1][1])
print('e -',  e[2][1])

#슬라이싱
print("#========#")
print('d -',d[0:3])
print('d -',d[2:])

#연산
