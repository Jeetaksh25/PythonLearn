from datetime import datetime
current_year=datetime.now().year
def age(DOB):
            a=int(DOB[4:])
            b=current_year-int(a)
            return b

DOB=input("Enter your DOB of format DDMMYYYY: ")

print(age(DOB))