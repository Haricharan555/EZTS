'''class sri:
    def _init_(self,name,age):
        self.name=name
        self.age=age
s=sri('srinivas',20)
print(s.name,s.age)'''

'''class sri:
    def _init_(self,name,age):
        self.name=name
        self.age=age
s1=input("enter name")
s2=int(input("enter age"))
print(s1,s2)'''

'''class sri:
    def _init_(self):
        self.name=input("enter name")
        self.age=int(input("enter age"))
s=sri()
print(s.name,s.age)'''

'''class A:
    def fun1(self):
        print("hii")
    #def fun3(self):        # making fun3 protected (abstraction)
        #print("how are you")
class B(A):
    def fun2(self):
        print("hello")
o=B()
o.fun1()
o.fun2()
#o.fun3()'''

'''class A:
    def _init_(self,a,b):
        self.a=a
        self._b=b
    def printB(self):
        print(slef._b)
o=A(10,20)
print(o.a,o._b)
#print(o._b)'''

'''class Student:
    def _init_(self):
        self.name = input("Enter name: ")
        self.usn = input("Enter USN: ")
        self.subjects = []
        self.marks = []
        self.percentage = None
        self.grade=None
        
        for i in range(2):
            sub = input("Enter subject name: ")
            mark = int(input("Enter marks: "))
            self.subjects.append(sub)
            self.marks.append(mark)
        
        smarks = sum(self.marks)
        self.percentage = (smarks / (len(self.marks) * 100)) * 100
        
        if self.percentage>=100 and self.percentage<90:
            self.grade='A'
        elif self.percentage>=89 and self.percentage<79:
            self.grade="B"
        elif self.percentage>=65 and self.percentage<50:
            self.grade="c"
        #else:
         #   self.grade="pass"

    def details(self):
        print(f"Name: {self.name}, USN: {self.usn}")
        for i in range(2):
            print(f"Subject: {self.subjects[i]}, Marks: {self.marks[i]}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"grade : {self.grade}")
        

o = Student()
o.details()'''



'''class Student:
    def __init__(self):
        self.name=input("Enter the name od the student:")
        self.usn=input("Enter the usn of the student:")
     
def subject():
    sub=input("enter the name of the subject:")
    sss.append(sub)
    return sub
def marks():
    
    ms=int(input("Enter the marks for the subjet:"))
    v.append(ms)
    if ((ms<0 ) or (ms>100)):
        print("invalid marks")
    else:
        print("Marks for the subject is:",ms)

s=Student()
print(s)  
v=[]
sss=[]
for i in range(5):
    subject()
    marks()
    print(sss)
    print(v)'''
    
