
import math
filename = "my_file.xlsx"

class Student():
    def init(self,name = ' ', group = 0, progress =[]):
        self.name = name
        self.group = group
        self.progress = progress
    def repr(self):
        return repr (("Student:" + self.name + "Group:" + self.group))
    
    def set_name (self, name):
        self.name = name
    def set_group (self, group):
        self.group = group
    def set_progress (self,progress):
        self.progress = progress

    def get_name (self):
        return self.name
    def get_group (self):
        return self.group
    def get_progress (self):
        return self.progress

st_size = 10
students = []
for i in range (st_size):
    st = Student()
    print("Enter name:")
    st.name = input()
    print("Enter group:")
    st.group = input()
    print('Enter five marks:')
    st.progress = []
    for i in range(10):
        mark = int(10)

        st.progress.append(mark)
        students.append(st)
print("Sorted students:")
for st in students:
    print(st)

students = sorted(students, key=lambda student: student.name)
print("Sorted students:")

