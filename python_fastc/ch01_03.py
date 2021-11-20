# 파이썬 심화
# 객채 지향 프로그래밍(oop) -> 코드의 재사용, 코드 중복 방지등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

#기본 인스턴스 메소드

class Student(object):
    '''
    Student class
    Author : Kim
    Date : 2021.07.03
    Description : Class, Static, Instance Method
    '''
    
#   class variable 클래스 변수
    tuition = 1.0
    
    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.grade = grade
        self.tuition = tuition
        self.gpa = gpa
    
    # self가 있으면 instance method 다
    # Instance Method
    def full_name(self):
        return '{},{}'.format(self.first_name, self.last_name)
    
    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {},{},{},{},{},{}'.format(self.id,self.full_name(),self.email,self.grade,self.tuition,self.gpa)
    
    def get_fee(self):
        return 'before tuition -> ID: {}, fee: {}'.format(self.id, self.tuition)
    
    def get_fee_culc(self):
        return 'after tuition -> ID: {}, fee:{}'.format(self.id,self.tuition*Student.tuition)
    
student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Sarang', 'student2@naver.com', '2', 500, 4.3)

print(student_1.full_name())
print(student_1.detail_info())
    
    
    
    
    
    
    
    
    
    