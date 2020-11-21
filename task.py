from statistics import mean
import json 
from dataclasses import dataclass, field
from itertools import repeat

class School:
    def __init__(self, name):
        self.name=name
        self.students={}

    def add_student(self, name, surname):
        self.students[(name, surname)]={}

    def add_student_class(self, name, surname, class_name):
        if not self.students[(name, surname)].get(class_name):
            self.students[(name, surname)][class_name]={'scores':[], 'attendance':[]}

    def add_student_score_class(self, name, surname, score, class_name):
        self.students[(name, surname)][class_name]['scores'].append(score)
  
    def add_student_attendance_class(self, name, surname, attendance, class_name):
        self.students[(name, surname)][class_name]['attendance'].append(attendance)
  
    def student_average_score(self, name, surname):
        temp = []
        keys = self.students[(name, surname)].keys()
        [temp.extend(self.students[(name, surname)][i]['scores']) for i in keys]
        return mean(temp)

    def student_average_score_class(self, name, surname, class_name):
        return mean(self.students[(name, surname)][class_name]['scores'])

    def average_score_class(self, class_name):
        temp = []
        [temp.extend(self.students[x][class_name]['scores']) for x in self.students]
        return mean(temp)
    
    def get_scores(self):
        temp = []
        [[temp.extend(self.students[x][i]['scores']) for i in self.students[x].keys()] for x in self.students]
        return temp

    def average_score(self):
        return mean(self.get_scores())

    def student_attendance(self, name, surname):
        temp = []
        keys = self.students[(name, surname)].keys()
        [temp.extend(self.students[(name, surname)][i]['attendance']) for i in keys]
        return sum(temp)

    def student_attendance_class(self, name, surname, class_name):
        return sum(self.students[(name, surname)][class_name]['attendance'])

    def get_students(self):
        result = list(map(lambda x: "\tname: {}, surname: {}\n".format(x[0], x[1]), self.students))
        result = ' '.join(result)
        return "SCHOOL: {}\n{}".format(self.name, result)

    def students_classes_results(self, name, surname, class_name):
        return "\tclass name: {}\n\t\tscores: {}\n\t\tattendance: {}\n".format(class_name,
                            self.students[(name, surname)][class_name]['scores'],
                            self.students[(name, surname)][class_name]['attendance'])

    def student_classes(self, name, surname):
        result = list(map(self.students_classes_results, repeat(name), repeat(surname), self.students[(name, surname)].keys()))
        result = ' '.join(result)
        return "name: {}, surname: {}\n {}".format(name, surname, result)

    def upload_from_file(self, file_name):
        data=json.load(open(file_name,))['data']
        for i in data:
            name=i['name']
            surname=i['surname']
            self.add_student(name, surname)
            for j in i['classes']:
                self.add_student_class(name, surname, j)
                for k in i['classes'][j]['scores']:
                    self.add_student_score_class(name, surname, k, j)
                for m in i['classes'][j]['attendance']:
                    self.add_student_attendance_class(name, surname, m, j)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            data=[]
            for x in self.students:
                data.append({"name": x[0], "surname": x[1], "classes":self.students[x]})
            json.dump(data, f)

@dataclass
class SchoolSystem:
    schools : list = field(default_factory=list)

    def find_student(self, name, surname):
        for i in self.schools:
            if i.students.get((name, surname)):
                return "name of school: {}\n{}".format(i.name, i.student_classes(name, surname))
    
    def find_schools_students(self, name):
        for i in self.schools:
            if i.name==name:
                return "name of school: {}\n{}".format(i.name, i.get_students())

if __name__ == "__main__": 
  schoolsystem = SchoolSystem()

  school1=School("school1")
  schoolsystem.schools.append(school1)

  school1.add_student("James", "West")
  school1.add_student("Jason", "Aston")

  school1.add_student_class("James", "West", "history")
  school1.add_student_class("James", "West", "math")
  school1.add_student_class("James", "West", "english")

  school1.add_student_class("Jason", "Aston", "english")

  school1.add_student_score_class("James", "West", 5, "history")
  school1.add_student_score_class("James", "West", 4, "math")
  school1.add_student_score_class("James", "West", 3, "math")
  school1.add_student_score_class("James", "West", 2, "english")
  school1.add_student_score_class("James", "West", 4, "math")
  school1.add_student_score_class("James", "West", 5, "english")

  school1.add_student_score_class("Jason", "Aston", 5, "english")
  school1.add_student_score_class("Jason", "Aston", 4, "english")
  school1.add_student_score_class("Jason", "Aston", 3, "english")
  school1.add_student_score_class("Jason", "Aston", 2, "english")

  school1.add_student_attendance_class("James", "West", True, "history")
  school1.add_student_attendance_class("James", "West", True, "history")
  school1.add_student_attendance_class("James", "West", False, "history")
  school1.add_student_attendance_class("James", "West", True, "math")
  school1.add_student_attendance_class("James", "West", False, "english")

  school1.add_student_attendance_class("Jason", "Aston", True, "english")
  school1.add_student_attendance_class("Jason", "Aston", False, "english")

  print(school1.student_attendance("James", "West"))
  print(school1.student_attendance("Jason", "Aston"))
  print(school1.student_attendance_class("James", "West", "history"))

  print(school1.student_average_score("James", "West"))
  print(school1.student_average_score("Jason", "Aston"))

  print(school1.student_average_score_class("James", "West", "math"))

  print(school1.average_score_class("english"))

  print(school1.get_scores())

  print(school1.average_score())

  school2=School("school2")
  schoolsystem.schools.append(school2)
  school2.upload_from_file("data.json")
  print(school2.get_students())

  print(school2.student_classes("Jesse", "King"))

  print(schoolsystem.find_student("Liam", "Pearce"))
  print(schoolsystem.find_student("James", "West"))

  print(schoolsystem.find_schools_students("school2"))

  school1.save_to_file("output_data.json")