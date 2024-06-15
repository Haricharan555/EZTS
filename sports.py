print("1.create_eq")
print("2.update")
print("3.Delete")
n=int(input("select any one from above three:"))

def create_equip():
    with open("sportclub.txt",'wb') as file:
        eq_id=str(input("Enter equipment id:"))
        eq_name=str(input("Equipment name;"))
        eq_condition=str(input("condition:"))
        eq_status=str(input("Status:"))
    
        s= f"{eq_id},{eq_name},{eq_condition},{eq_status}\n"
        file.write(s.encode())
result=create_equip()


    

