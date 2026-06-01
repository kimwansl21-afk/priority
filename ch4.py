jumin= '123456' #jumin=1234567 했더니 오류// 문자열만 인덱스 사용
jumin='031021-1234567'

year=jumin[:2]
month=jumin[2:4] 
day=jumin[4:6]

'''슬라이싱에서 종료 인덱스 이전까지 가져옴;; // docstring
'''

gender=jumin[7] #인덱싱,, 하나 가져오기
'''
a=jumin[-7:]; print(a)
a=jumin[-14]; print(a)   음수인덱스는 -1부터 ㅅㅣ작
a=jumin[:-7]; print(a)
a=jumin[-7:]; print(a)
a=jumin[-7:]; print(a)
a=jumin[-7:]; print(a)
a=jumin[-7:]; print(a)
print(a)
'''


# print(f"생년원일은 20{year}년 {month}월 {day}일")

# # if gender=='1' :  #if 로 가져올때도 '1'로 해야됨 문자열이니깐
#  print('woman')
# else :
#  print('man')
# # print(type(year))     print(type(year)) 숫자가 와도 문자열로 인식 인덱스니깐



# 내부코드 들여쓰기 else는 해당 안됨

# print(filename.index('l'))   l등장 위치마다 인덱스 하려면 반복문을 배워야한다


# print(data[1]) 리스트에서 1번인덱스 가져오기 

# print(len(filename)) 변수의 문자열 개수 파악 띄어쓰기 포함

# print(filename.count('l'))

# if filename.count('l')>=3 :
    # print('l이 너무 많아')
# 
# print(filename.lower())    


# print(filename.upper())


# print(filename.islower())    


# filename='FFSDfdsFds'
# print(filename[:5].isupper())    

# print(filename.split('f') )

# a='apple'

# print(a.replace('apple','banana'))

# msg=input("메시지 입력:")

# msg=msg.replace('병신새끼야','****야')

# print(msg)
# python='Python is amazing'

# # print(python[6])  공백도 인덱스 포함

# find=python.find('n')

# find=python.find('n',find+1)

# find=python.find('java')

# print(find)

len('hello')
print(len('hello'))

# print('hello\n  today contents is\n itall')  탈출문자 줄바꿈 역슬래시n

# a=122

# print(a,'my name is','wansu kim',sep='    ')


# print('안녕하세요{0}저는 {1}입니다'.format('반갑습니다','김완수'))  ,format이 아니라 .format

# print('hello %d fsdfs',(3102)) 문자열 통째로 안에 %d ()사용 표현

# a='안녕하세요'

# print(f'{a} my name is wansu kim')



'''
 print('나는 %d살입니다' % 24)

 print('%s %s '% ('안녕하세요 제 나이는','20이에요'))

 print('%c' %'5')
 2026-05-24 // 서식지정자
'''
