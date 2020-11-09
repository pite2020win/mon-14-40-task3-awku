class School:
  def __init__(self, name):
    self.name=name
    self.students={}
    self.classes=[]

  def add_student(self, name, lastname):
    self.students[(lastname, name)]={}
  
  def add_class(self, name):
    self.classes.append(name)
  
  def add_student_class(self, name, lastname, classid):
    self.students[(lastname, name)][classid]=[[],[]]

  def add_student_score_class(self, name, lastname, score, classid):
    (self.students[(lastname, name)][classid][0]).append(score)
  
  def add_student_attendance_class(self, name, lastname, attendance, classid):
    (self.students[(lastname, name)][classid][1]).append(attendance)
  
  def student_average_score(self, name, lastname):
    avg=0
    c=0
    for k,v in self.students[(lastname, name)].items():
      avg+=sum(v[0])
      c+=len(v[0])
    return avg/c

  def student_average_score_class(self, name, lastname, classid):
    avg=sum(self.students[(lastname, name)][classid][0])
    return avg/len(self.students[(lastname, name)][classid][0])

  def student_attendance(self, name, lastname):
    att=0
    for k,v in self.students[(lastname, name)].items():
      att+=sum(v[1])
    return att

  def student_attendance_class(self, name, lastname, classid):
    return sum(self.students[(lastname, name)][classid][1])
  
if __name__ == "__main__": 
  school=School("school1")
  school.add_class("history")
  school.add_class("math")
  school.add_class("english")

  school.add_student("James", "West")
  school.add_student("Jason", "Aston")

  school.add_student_class("James", "West", 0)
  school.add_student_class("James", "West", 1)
  school.add_student_class("James", "West", 2)

  school.add_student_class("Jason", "Aston", 2)

  school.add_student_score_class("James", "West", 5, 0)
  school.add_student_score_class("James", "West", 4, 1)
  school.add_student_score_class("James", "West", 3, 1)
  school.add_student_score_class("James", "West", 2, 2)
  school.add_student_score_class("James", "West", 4, 1)
  school.add_student_score_class("James", "West", 5, 2)

  school.add_student_score_class("Jason", "Aston", 5, 2)
  school.add_student_score_class("Jason", "Aston", 4, 2)
  school.add_student_score_class("Jason", "Aston", 3, 2)
  school.add_student_score_class("Jason", "Aston", 2, 2)

  school.add_student_attendance_class("James", "West", 1, 0)
  school.add_student_attendance_class("James", "West", 1, 0)
  school.add_student_attendance_class("James", "West", 0, 0)
  school.add_student_attendance_class("James", "West", 1, 1)
  school.add_student_attendance_class("James", "West", 0, 2)

  school.add_student_attendance_class("Jason", "Aston", 1, 2)
  school.add_student_attendance_class("Jason", "Aston", 0, 2)
  
  print(school.student_attendance("James", "West"))
  print(school.student_attendance("Jason", "Aston"))
  print(school.student_attendance_class("James", "West", 0))

  print(school.student_average_score("James", "West"))
  print(school.student_average_score("Jason", "Aston"))

  print(school.student_average_score_class("James", "West", 0))
  print(school.student_average_score_class("Jason", "Aston", 2))
