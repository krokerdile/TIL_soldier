# 점프 투 파이썬 페이지를 보고 파이썬을 완전 기초 부터 하나씩 정리해보자

# 숫자형이란 숫자 형태로 이루어진 자료형

# 정수형이란 말 그대로 정수를 뜻하는 자료형을 말한다.
# a=123
# print(a)
# a=-178
# print(a)
# a=0
# print(a)

# 실수형(Floating Point)
# a=1.2
# print(a)
# a=-3.45
# print(a)

# 8진수와 16진수
# a=0o1777
# print(a)
# a=0x8ff
# print(a)

# 숫자형을 활용하기 위한 연산자
# a=30
# b=4
# # 덧셈
# print(a+b)
# # 뺄셈
# print(a-b)
# # 제곱
# print(a**b)
# # 나눗셈 후 나머지를 반환하는 % 연산자
# print(a%b)
# # 나눗셈 후 몫을 반환하는 // 연산자
# print(a//b)

# 문자열이란 문자,단어 등으로 구성된 문자들의 집합을 의미한다. 
# print("life is too short, you need python")
# print("a")
# print("123")

# >>> 따옴표로 둘러싸여져 있으면 모두 문자열이라고 보면 된다.

# 문자열을 만드는 방법
# print("Hello world!")
# print('python is fun')
# print("""life is too short""")
# print('''life is too short''')

# 문자열에서 "와 ' 둘다 사용하는 이유
# 서로를 구분해서 사용하여주기 위해서
# ex)
# print("hello it's me")
# print('hello it"s me')
# 예시로는 조금 잘못 되었을 수도 있지만 이런식으로 사용을 할 수도 있고
# \ 백슬래시를 사용해서도 할 수 있다.
# print('python\'s favorite food is perl')
# print("\"python is very easy\"")

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# smp = "Life is too short \nYou need Python"
# print(smp)

# 요런 느낌으로 만들 수 있지만 읽기에 불편하고 줄이 길어지는 단점이 있음
# smp='''Life is too short
# So You need Python'''
# print(smp)
# 이렇게 써주면 짧게 문자열을 가독성 있게 작성할 수 있음
# 참고로 이거 왜 파이썬 2년을 썻는데 처음 아는 거 같냐..?

# 문자열 더해서 연결하기
# head = "head"
# tail = "tail"
# print(head+tail)

# 요런 느낌으로 문자열을 "+"를 이용하여서 붙여서 만들어 줄 수가 있다.

# 몰랐는데 곱하는 방법도 있다
# smp = "sample"
# print(smp*2)

# 문자열에 대해서 몰랐던 부분이 많지 않았나라는 생각을 가지게 하는 거 같다.

# 그래서 예를 들면 이런 식으로 코딩을 할 수 있다고 한다.
# print("="*50)
# print("이런 식이랄까?")
# print("="*50)

# 원래 알고 있었지만 빠트렸던 간단한 내용들이 많은 거 같다.

# 문자열 길이를 구하는 방법은 
# a = "hellomynameisjacky"
# print(len(a))
# 이런식으로 한다.

# 문자열인덱싱과 슬라이싱
# 만약에 문자열의 예시로
# a = "Life is too short, so You need Python"
# 이라고 한다면
# L은 0번쨰 자리이고 t는 16번째 자리를 맞는 친구일 것이다.
# 이건 뭐랄까 배열에서 몇 번째 칸이 몇 번인지 아는 느낌이랄까

# print(a[3])

# 문자열 슬라이싱 -> 문자열에서 위에 처럼 인덱스를 통하여서 한 문자만을 뽑는 것이 아니라 일부를 잘라내는 방법이라고 볼 수 있다. 
# a = "Life is too short, so You need Python"

# print(a[0:4])
# 여기서 a는 인덱스로 따지마면 0<=a<4 사이에 있다고 볼 수 있을 것이다. 
# print(a[-8])
# 마이너스를 사용하게 되면 뒤에서 부터 빼서 계산을 하여 주는 거 같다.
# n0o1h2t3y4p5 6d7 이건 뭔가 헷갈리긴 하지만 잘 사용하지는 않을거 같긴하다. 

# c언어에서 print("%d",&x)라고 사용했던 것과 같이 
# 파이썬에서는 해당 개념을 포매팅이라고 한다. 

# print("I eat %d apples" % 3)
# 요런 느낌으로 사용하여 줄 수가 있다. 
# 숫자 뿐만 아니라 변수나 문자열도 넣을 수 있고
# 두 개 이상을 포매팅할 수도 있다.
# print("I eat %d apples and %d perls" %(5,10))

# 그리고 format 함수를 통해서도 넣을 수 있는데
# print("I eat {0}apples and {1}pies".format(5,10))
# 그리고 애초에 변수를 만들어서
# name="홍길동"
# age="10"
# print(f'나의 이름은 {name}이고 저는 {age}살입니다')
# 로도 할 수 있다는 점은 원래 몰랐었쥬..?

# 리스트 자료형
# 배열처럼 사용할 수 있는 파이썬의 자료형이랄까

# 리스트는 다양하게 존재할 수 있다.
# a = []
# print(a)
# a=[1,2,3]
# print(a)
# a=[1,2,['life','is']]
# print(a)
# 처럼 그냥 비어 있을 수도 있고 숫자가 들어갈 수도 있고 리스트 안에 리스트가 있을 수도 있다. 

# a=[1,2,3]
# print(a[0])

# 처럼 인덱스를 통해서 찾을 수도 있다.

# 만약에 리스트가 
# a = [1,2,3,['a','b','c']]
# # 라고 되있다면
# print(a[-1][0])
# 로도 사용할 수가 있다

# 이중, 삼중 그 이상도 가능하긴 하다.
# 앞에서의 문자열 처럼 더하고 나누고 슬라이싱이 동일하게 가능하고, 
# a=[1,2,3]
# print(a*3)
# print(a+a)
# print(len(a))

# 값의 삭제도 가능하다.
# a=[1,2,3]
# del a[2:]
# print(a)

# 추가하는 함수는 리스트.append()
# 정렬하는 함수는 리스트.sort()
# 뒤집는 함수는 리스트.reverse()를 하여 주면 된다. 
# index 함수는 괄호 안의 값이 존재를 하는지 확인하고 있다면 그 값의 자리를 알려준다
# a = [1,2,3]
# print(a.index(2))
# a=[1,2,3,4,2]
# print(a.index(2))
# 1,1로 자리를 알려주는데 이때 맨 처음에 찾은 값에 대해서 알려준다는 것을 유의할 수 있도록 하자.

# 그리고 중간에 자리를 선택하여서 넣는 함수는 insert() 함수 이다.
# a=[1,2,3]
# a.insert(1,2)
# print(a)
# remove 함수는 index 함수 처럼 첫번째로 찾아서 나오는 괄호 안의 값을 지우는 함수이다. 
# print(a.remove(1),a)

# 처럼 값이 나오는 것을 확인 할 수가 있다. 
# Queue의 기능인 pop을 여기서도 사용할 수 있는데
# a=[1,2,3]
# print(a.pop(1))
# 요렇게 사용하여 주면 괄호 안의 값을 뺼수도 있고 그냥 pop()으로 사용하게 되면 우리가 알고 있는 pop()과 동일한 기능을 하여준다.

# 그리고 리스트 안에 원하는 값이 몇개가 있는지 궁금하다면 count()를 통하여서 확인을 할수 있다.
# a=[12,2,2,2,2,2,2,2,3]
# print(a.count(2))

# 그리고 리스트에 대해서 리스트를 추가 하고 싶다면 
# a=[1,2,3]
# b=[4,5]
# print(a.extend(b),a)
# 이런식으로 사용을 하여 줄 수가 있다. 
# 사실 그냥 + 쓰는 거랑 똑같다. 

# 튜플 자료형
# 튜플은 리스트와 유사하지만
# 1. 괄호 ()로 둘러싸인 다는 점에서 차이가 있고
# 2. 값을 바꿀 수가 없다는 점에서 차이가 있다고 볼 수 있다. 

# 전에 고정형으로 변수를 선언하는 거를 다른언어(c언어나 Java에서 배웠던 거 같은디)에서 배웠는데
# 걔네와 아마 느낌이 비슷하다고 볼 수 있고
# 리스트와 동일하게 슬라이싱, 더하기, 곱하기, 길이 구하기, 인덱스로 값 찾기는 가능하다. 

# 딕셔너리
# 사람에게 이름 = 홍길동, 생일 = 8/31 등 대응관계를 나타내는 정보들이 있다. 파이썬도 이런 대응관계를 나타내는 자료형을 가지고 있는데
# 그것이 바로 딕셔너리 이다. 다른 언어에서는 이를 해쉬 혹은 연관 배열이라고 한다.
# 딕셔너리는 그래서 KEY와 그에 대응되어지는 Value 값을 가지고 있는 자료 형이다. 
# dic = {'name':'jacky','birthday':'0831'}
# print(dic)
# 대응되어지는 value에는 숫자를 넣을수도, 문자열을 넣을수도 있고, 그리고 리스트를 넣을수도 있다. 
# 딕셔너리의 상을 추가하는 방법은 우리가 배열의 인덱스를 사용하는 것 처럼
# a={'a':1,'b':2}
# a['c']=3
# print(a)
# 이런식으로 사용하여 줄 수 있고 삭제는 del 딕셔너리[]로 하여주면 된다. 
# 딕셔너리를 사용하는 방법에는 주로 여러 데이터와 형식을 저장할 때 특정 데이터를 보여줄 때 사용하여 준다고 볼수 있다.(내가 봤을떈 아마도?)
# a = {"김연아":"피겨스케이팅","류현진":"야구"}
# print(a["김연아"])
# /처럼 사용을 하여 줄 수 있다
# 딕셔너리를 사용할 때 유의하여야 되는 점은 Key값은 고유한 값이무로 동일한 키값이 존재하였을 때 
# a = {1:'a',1:'b'}
# print(a)
# 처럼 뒤에 넣어진 값이 덮어 씌우는 것을 확인 할수가 있다. 
# key 값이 고유한 값이기 때문에 불변한 값들만 키값으로 사용할 수 있다.
# 그 의미는 리스트 처럼 바뀔 수 있는 값은 사용을 할 수 없다는 의미이고
# 다르게 보면 튜플 처럼 값이 바뀌지 않는 다면 키 값으로 사용 할 수가 있다는 것이다. 

# 딕셔너리에도 다양한 함수들이 존재를 하는데 
# 우선적으로 key들의 리스트를 뽑아주는 keys()가 있다.
# a={'1':'a','2':'b','3':'c'}
# print(a.keys())
# 그리고 반대로 value들의 리스트를 뽑아주는 values()또한 있다.

# 그리고 원하는 key에 해당하는 값을 뽑는 get()있다.
# print(a.get('1'))
# 만약에 원하는 값이 없을 경우 원하는 디폴트 값, 그니까 없을 경우에 return -1을 해주는 거 처럼 미리 값을 설정해두면 편한데
# 이를 get(x,'디폴트')로 하여주면 된다.
# print(a.get('5','없넹'))
# 그리고 index 처럼 안에 값이 있는지 확인 하는 방법으로 in을 사용하면 된다.
# print('5' in a) 이런 식으로 사용하여 주면 된다.

# 집합 자료형
# 집합에 관련된 것을 쉽게 처리하기 위해서 만든 자료형이라고 한다.

# s1 = set([1,2,3])
# print(s1)

# 집합 자료형의 경우 몇가지 특징이 있다.
# 1. 중복 같은 건 허용하지 않는다.
# 2. 순서가 없다. 

# 리스트나 튜플의 경우에 인덱스를 통해서 순서가 있는 자료형임을 알 수 있지만
# 집합 자료형의 경우에 순서가 없기 때문에 인덱싱으로 값을 알수가 없다.
# + 딕셔너리도 순서가 없는 자료형이기 때문에 인덱스를 통해서 값에 접근을 할 수가 없다고 볼 수 있다. 

# s1 = set([1,3,4,34,344])
# print(s1)

# set의 경우에 print()를 하면 순서대로 나오는 걸로 알고 있었는데 아닌가벼
# s1 = set([3,44,4444,2,1])
# print(s1)
# 근데 또 하니까 순서대로 나오는거 같긴핟.
# 교집합은 &을 통해서
# 합집합은 |을 통해서 구할 수 있다. 
# 합집합은 |말고도 union()함수를 통해서도 구할 수 있다. 

# s1=set([1,2,3])
# s2=set([4,5,6])
# print(s1.union(s2))

# 차집합은 -를 이용하거나 difference()를 이용하여 주면 된다.
# 1개의 값을 추가할 때는 add()를 여러개의 값을 동시에 추가할 때는 update를 사용하여 주면 되고
# 다른 자료형과 마찬가지로 특정값을 제거할 때는 remove를 사용하여 주면 된다. 

# 변수를 어떻게 만들까?
# 변수를 만들 때는 "변수명" = (assignment)를 사용한다.
# 파이썬은 c,java와는 달리 스스로 값을 판단하여 자료형을 지정하기 때문에 더 편리하다.

# 파이썬에서 변수를 만들었을 때 
# a = [1,2,3]
# print(id(a)) 
# 처럼 메모리 값을 id(*)를 통해서 확인 할 수 있습니다.

# 만약 a=[1,2,3]이라는 리스트와 b=a 가 있다면 a와 b는 같은 것일 까?
# a=[1,2,3]
# b=a
# print(id(a))
# print(id(b))

# 를 보면 알 수 있듯이 완전히 동일한 리스트를 a,b가 참조 하고 있음을 알 수 있습니다.
# 그래서 만약 b변수를 생성했을 때 a 변수를 참조하면서 다른 주소를 가리키도록 하려면 어떻게 해야 할까?
# 1. [:]이용
# a=[1,2,3]
# b=a[:]
# a[1] = 4
# print(a)
# print(b)

# 이런식으로 a 리스트안의 내용을 복사하여서 넘겨줄 수 있다.
# 그리고 b=a[:]는 b=copy(a)와 동일합니다.
# copy()를 사용하려면 from copy import copy를 사용하여 줘야 합니다.
# 이렇게 하여주면 b is a 를 하였을 때는 False가 나오게 됩니다. 

# if문
# 조건문, 일어날 수도 있는 상황을 제어하여 주기 위해서는 if문을 사용하여 주어야 합니다.
# money = True
# if money:
#     print("나는 돈이 있다.")
# else: 
#     print("나는 거지다")
# 처럼 돈이 있는지 없는 지를 판단해주기 위해서 조건문을 사용하게 됩니다. 
# 중요한 것은 if 조건문을 작성하여줄 때 반드시 : 콜론을 붙여 주어야 한다는 것 + 들여쓰기를 잘해야 하는 것
# 다른 언어와 동일하게 or and not을 사용하고 다른언어와 달리 글자 그대로 붙여서 사용한다는 점이 차이 입니다.
# 그리고 안에 있는지 없는 지를 in 과 not in을 통해서 확인을 하여 줄 수 있습니다.   

# if 'a' in ('a','b','c'):
#     print(True)

# 이런식으로 적용을 할 수가 있다. 
# 그리고 c언어에서 continue에 해당하는 기능을 pass를 통해서 사용할 수가 있다.

# pocket = ['paper','money','cellphone']
# if 'money' in pocket:
#     pass
# else:
#     print("카드를 꺼내라")


# for i in range(10):
#     if i % 2 == 0:
#         pass
#         print(i)    
#     else:
#         print(i)
# print("Done")

# pass는 넘어가는 용도?
# pass가 사용되는 경우는 1. 조건문에서 넣어줄 조건이 딱히 없을경우, 2. class 선언할 때, 초기에 넣어줄 값이 없을 때 정도로 생각할 수 있을 것 같습니다.
# 일단 코드를 작성한 후 동작 확인을 위해서 실행할 때, 해당 부분에서 오류가 발생하지 않도록 하기위해 많이 사용한답니다. 라고 
# https://chancoding.tistory.com/7 에서 설명을 해주고 있어서 일단 이렇게 이해를 하면 될 거 같습니다. 

 

# for i in range(10):
#     if i % 2 == 0:
#         continue
#         print(i)    
#     print(i)
# print("Done")

# continue는 c언어에서 사용했던 것과 동일하게 그 밑의 단계를 넘어가주는 것으로 생각하여 주면 되고

# for i in range(10):
#     if i % 2 == 0:
#         break
#         print(i)    
#     else:
#         print(i)
# print("Done")

# break는 해당 조건이 만족하면 종료가 되는 것으로 동일하게 이해 하여 주면 됩니다.

# pocket = ['paper','handphone']
# card = True
# if 'money' in pocket:
#     print("택시를 타고가라")
# else: 
#     if card:
#         print("택시를 타고가라")
#     else: 
#         print("걸어가라")

# 로 적으면 전반적으로 코드가 붕 뜨는 것을 알 수 있다. 산만해져 보이고

# 그래서 elif(타 언어에서는 else if로 쓰는 것을) 지원 하여 준다.

# pocket = ['paper','cellphone']
# card = True

# if 'money' in pocket:
#     print("택시를 타고가라")
# elif card:
#     print("택시를 타고가라")
# else: 
#     print("걸어가라")

# c언어에서의 언어처럼 조건부로도 적을 수 있는데
# score = 70
# message = "success" if score >= 60 else "failure"

# 조건 표현식을 조금이나마 자연스럽게 쓰는 방법은 지능형 리스트와 같이 활용하는 것입니다. 이외에는 실전에서 그렇게 많이 사용되지는 않습니다. 라고 (https://elvanov.com/1770) 블로그에서 말씀하신거 참고

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit +1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")

# while문은 while문 옆에 있는 조건문을 만족 할 때까지 반복을 하게 해주는데
# 조건에 들어갈 수 있는 경우는 다양하게 있습니다.

# 예를 들어서 number != 4 도 조건에 넣어서 사용할 수 있습니다. 
# prompt="""
# 1. ADD
# 2. DEL
# 3. LIST
# 4. QUIT
# Enter number : """
# number =0
# while number !=4:
#     print(prompt)
#     number = int(input())

# 그리고 강제로 while문을 중간에서 종료 해주고 싶다면 break를 통해서 종료를 시키면 된다. 

# a=0
# while a < 10: 
#     a = a+1
#     if a%2 == 0: continue
#     print(a)
        
# for문
# test_list = [1,2,3]
# for i in test_list:
#     print(i)

# continue문을 for문에서도 사용하여 줄 수 있는데 여기서도 continue를 만나면 for문의 맨 처음으로 돌아가게 된다.

# 그리고 in과 함께 range()를 자주 함께 사용하는데
# a = range(0,10)
# for i in a:
#     print(i)
# 런 식으로 사용해주면 0에서 부터 10미만 까지의 값을 가지고 있는 range 객체를 만들어 주는 것이다. 

# 파이썬 함수

# def 함수명(매개변수):
    # 문장
#     실행할 문장

# def add(a,b):
#     return a+b

# print(add(1,2))

# 처럼 작성을 하여서 만들어 줄 수 있고, 여기서 return은 결과값을 돌려주는 명령어 입니다. 
# 입력값이 없는(인수가 없는 함수)도 존재할 수 있으며, 결과 값이 없는 함수 또한 존재 할 수도 있습니다. 
# def add(a, b): 
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# 처럼 결과값 없이 그대로 출력하여 주는데 사용하여 주기도 합니다. 

# def add_many(*args): 
#     result = 0 
#     for i in args: 
#          result = result + i 
#     return result 
 
# result = add_many(1,2,3,4,5)
# print(result)

# 사용자의 입력
# a=input()
# print(a)

# number = input("숫자를 입력하세요")
# print(number)

# print("life""is""too short")

# print("life","is","too short")
# 쉼표 한개는 띄어쓰기가 되는데 두개는 안된다는 점 

# for i in range(10):
#     print(i,end='\n')

# 끝문자를 위의 경우 처럼 지정하여 줄 수 있다는 점

# 클래스

# 자바에서 배웠던 개념이지만 여전히 좀 헷갈리는?

# result1 = 0
# result2 = 0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

# 동일한 역할을 해줄 수 있는 객체를 만들어주는 것이 클래스?
# 대신에 각각의 객체는 서로에게 전혀 영향을 주지 않는다는 점?

# 그래서 클래스를 쿠키틀에 비유하고 객체를 쿠키에 비교하는 거
# A라는 클래스에 의해 만들어진 B 객체는 A의 인스턴스라고 할 수 있다는 점

# class FourCal():
#     def __init__(self, ):
#         self.result=0
        
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
        
#     def add(self):
#         self.result = self.first + self.second
#         return self.result
    
# a = FourCal()
# a.setdata(1,2)
# print(a.add())

#  def __init__(self, ):
        # self.result=0
    
# 여기서 self는 클래스를 통해서 생성되어지는 객체를 이야기 하고 
# 만약 그 뒤에 (self, first, second)를 넣고 
# self.first = first를 넣게 된다면 
# 클래스를 통해서 만들어진 객체에 변수를 더해주는 것이기 때문에 객체 변수가 생성되어 진다.
# 그리고 __init__은 객체를 만들어줄 때 처음에 자동으로 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되어진다.

# 클래스를 상속시키고 싶다면 class MoreFourCal(FourCal) 이런식으로 작성을 하여주면 상속을 시켜줄 수 있다.
# 상속을 시켜주는 이유는 
# 1. 기존 클래스를 변경하지 않고 기능을 추가한 클래스가 필요해서
# 2. 기존 기능을 변경하여 주기 위해서 
# >>> class SafeFourCal(FourCal):
# ...     def div(self):
# ...         if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
# ...             return 0
# ...         else:
# ...             return self.first / self.second

# 그리고 기존 기능을 변경 하여 주기 위해서 메서드 오버라이딩을 사용할 수도 있다.
# 그리고 객체 변수가 있었듯이 클래스에도 변수가 있다.
# class Family:
#     lastname = "김"
    
# print(Family.lastname)

# 이런 식으로 클래스에도 자체적으로 클래스 변수를 만들어 줄 수가 있다. 

