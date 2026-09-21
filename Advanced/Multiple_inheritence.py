class Teacher():
    def teacher_action(self):
        print('I can teach !')



class youtuber():
    def youtuber_action(self):
        print('I can make videos !')

class Student(Teacher,youtuber):
    def action(self):
        print('I can Study')

x = Student()
x.action()
x.teacher_action()
x.youtuber_action()
