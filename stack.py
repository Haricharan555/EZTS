'''class stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        self.items.pop()
    def size(self):
        return len(self.items)
    
s=stack()
s.push(10)
print(s.items)
s.pop()
print(s.items)
s.size()'''

'''e=input()

s=[]

flag=0
for i in e:
    if i=='[' or i=='{' or i=="(":
        s.append(i)
    if i==']' or i=='}' or i==')':
        x=s.pop()
        if x == "(" and i ==")":
            pass
        elif x == "{" and i =="}":
            pass
        elif x == "[" and i =="]":
            pass
        else:
            flag=1
            break
            
if (flag==0 ):
    print("valid")
else:
    print("invaid")'''

'''s = stack()
e = input("Enter expression: ")

ob = "[{("
cb = "]})"
flag = 0

for i in e:
    if i in ob:
        s.push(i)
    elif i in cb:
        x = s.pop()
        if x is None:  # Check if stack is empty
            flag = 1
            break
        if (x == "(" and i == ")") or (x == "{" and i == "}") or (x == "[" and i == "]"):
            pass
        else:
            flag = 1
            break

if flag == 0 and s.size()==None:
    print("valid")
else:
    print("invalid")'''

'''l=[3,5,7,2]
m=0
x=[]
for i in range(0,len(l),-1):
   
    if l[i+1]<=l[i]:
        m=l[i]
        x.append(m)
        print(x)
    else:
        m= -1
        x.append(m)
print(x)'''





