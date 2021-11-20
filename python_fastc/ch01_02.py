# 파이썬 심화
# 객채 지향 프로그래밍(oop) -> 코드의 재사용, 코드 중복 방지등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Student():
    """
    Student Class
    Author : hyunwoo
    Date : 2021.06.27
    """
    
    # 클래스 변수
    student_count = 0
    
    def __init__(self, name, number, grade, details, email=None):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self.email = email
        
        Student.student_count += 1
    
    def __str__(self):
        return 'str {}'.format(self._name)
#     ->위의 문장이 어떤 식으로 작용하는지 공부해서 적어두기

    def __repr__(self):
        return 'repr {}'.format(self._name)
    
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info: {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1


studt1 = Student('Cho',2,3,{'gender':'Male','score1':65,'score2':42})
studt2 = Student('Cho',2,3,{'gender':'Male','score1':65,'score2':42})

print(id(studt1))
print(id(studt2))

print(studt1)
print(studt2)

print(dir(studt1))