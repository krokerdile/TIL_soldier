student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1

student_detail_1 = [
    {'gender' : 'male'},
    {'score1' : 95},
    {'score2' : 88}
]

# 이렇게 코드를 짜면 절차지향 적으로 위에서 부터 아래로 단순하게 코드를 읽고 작동하게 됨
# 병원에서 쓰는 프로그램의 경우에는 이런식으로 많이 짜여지는데, 그런 것들은 범용적으로 데이터를 많이 담아서 쓰는데는 맞지 않음

student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2

student_detail_2 = [
    {'gender' : 'Female'},
    {'score1' : 95},
    {'score2' : 88}
]

student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 3

student_detail_3 = [
    {'gender' : 'male'},
    {'score1' : 95},
    {'score2' : 88}
]

#리스트 구조
student_names_list = ['Kim','Lee','Park']
student_numbers_list = [1,2,3]
student_grades_list = [1,2,3]
student_details_list =[
    {'gender':'Male','score1':95, 'score2':88},
    {'gender':'Male','score1':95, 'score2':88},
    {'gender':'Male','score1':95, 'score2':88}
    
]

del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list, student_numbers_list, student_grades_list, student_details_list)


# 우리가 리스트 형태나 디셔너리 형태로 만드는 형태로 코드를 짜야지 직접 이렇게 만들어서 사용하는 경우는 줄어야 될 필요가 있음
# 그리고 단순히 이런식으로 전체가 나눠진 리스트 형태로 구조를 짜게 되면 각각의 리스트를 관리하는데 따로 리소스가 들기 때문에 불편해
# 지고 전반적인 코스트가 올라갈 수 밖에 없음

#딕셔너리 구조
students_dicts = [
    {'student_name':'Kim','student_number':1,'student_grade':1, 'student_detail':{'gender':'male','score1':90}},
    {'student_name':'Kim','student_number':1,'student_grade':1, 'student_detail':{'gender':'male','score1':90}},
    {'student_name':'Kim','student_number':1,'student_grade':1, 'student_detail':{'gender':'male','score1':90}}
]

del students_dicts[1]
print(students_dicts)

# 리스트에서 딕셔너리 형태로 바꾸게 되면 좀 더 사용하기 편하다는 장점이 있지만
# 반복되는 코드가 몇개 있고, 중첩 문제가 생기게 된다. 
# django에서 omr을 사용할 때도 이런식으로 데이터를 뽑아 오게 됨.
# 다른 곳에서 데이터를 받아오면 이런식으로 많이 받아 올때가 있음

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
# 옛날 보다 cpu, 메모리의 성능이 좋기 때문에 클래스를 사용해도 괜찮음

# class Student(object)로 작성해줘도 된다.
class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number 
        self._grade = grade
        self._details = details
    
    def __str__(self):
        return 'str:{}'.format(self._name)
    
    def __repr__(self):
        return 'repr:{}'.format(self._name)

student1 = Student('Kim',1,1, {'gender':'male','score1':90})
student2 = Student('Kim',1,1, {'gender':'male','score1':90})
student3 = Student('Kim',1,1, {'gender':'male','score1':90})
print(student1.__dict__)
print(student1)

student_list = []
student_list.append(student1)
student_list.append(student2)
student_list.append(student3)

print(student_list)