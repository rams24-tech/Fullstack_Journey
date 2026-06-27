class Student:
    def __init__(self,name):
        self.name=name
        self.grades=[]
    def add_grade(self,grade):
        self.grades.append(grade)
        print(f"Grade {grade} added for {self.name}")

    def get_average(self):
        avg=0
        
        if len(self.grades)!=0:
            for i in self.grades:
                avg=avg+i
            avg=avg/len(self.grades)
        else:
            avg=0
                   
        return avg
             
    
    def __str__(self):
        return f"- {self.name} - Average: {self.get_average()}"
        

class Classroom():
    def __init__(self,subject):
        self.subject=subject
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
        print(f"{student.name} added to {self.subject} class")
    def show_results(self):
        print(f"{self.subject} Results:")
        for i in self.students:
            print(str(i))
            
    def top_student(self):
        best = self.students[0]
        for i in self.students:
            if i.get_average() > best.get_average():
                best=i 
        print(f"Top student: {best.name} with average {best.get_average()}")              

classroom = Classroom("Math")

s1 = Student("Kasi")
s2 = Student("Vinay")
s3 = Student("Chitti")

s1.add_grade(85)
s1.add_grade(90)
s2.add_grade(95)
s2.add_grade(87)
s3.add_grade(78)
s3.add_grade(82)

classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(s3)

classroom.show_results()
classroom.top_student()
