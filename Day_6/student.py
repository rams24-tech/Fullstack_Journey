class Student:
    def __init__(self,name):
        self.name=name
        self.grades=[]

    def add_grade(self,grade):
        self.grades.append(grade)
        print(f"Grade {grade} added for {self.name}.")

    def get_average(self):
        if len(self.grades)==0:
            print("No grades recorded yet.")
        else:
            total=0
            for i in self.grades:
                total=total+i
            avg=total/len(self.grades)
            print(f"{self.name}'s average:{round(avg,2)} .")  

    def show_grades(self):
        print(f"{self.name}'s grades:{self.grades[::1]}") 

stu_1=Student("Kasi") 
stu_2=Student("vinay")      
stu_1.get_average()
stu_1.add_grade(90)
stu_1.add_grade(86)
stu_1.add_grade(70)
stu_1.add_grade(79)
stu_2.add_grade(93)
stu_2.add_grade(90)
stu_2.add_grade(86)
stu_2.add_grade(70)
stu_2.add_grade(79)
stu_2.add_grade(93)

stu_1.get_average()
stu_2.get_average()

stu_1.show_grades()          
stu_2.show_grades()     