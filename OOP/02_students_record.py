"""
2. Student's Record
"""

class Student:
    def __init__(self,name,marks):
      self.name=name
      self.marks=marks

    def avg_marks(self):
      avg=sum(self.marks)/len(self.marks)
      if avg>=40:
        print(f"{self.name} passed with an avg of {avg}")
      else:
        print(f"{self.name} failed with an avg of {avg}")
      return avg

    def display_info(self):
      print(f"Student:{self.name}, Marks:{self.marks}")

stud=input("Enter the name of the student: ")
mark=list(map(int,input("Enter the marks of {stud} separated by space: ").split()))

student_info=Student(stud,mark)
student_info.display_info()

n=int(input("Enter the new mark: "))
mark.append(n)

student_info.avg_marks()
