class Student:
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
    print(v)
    






   