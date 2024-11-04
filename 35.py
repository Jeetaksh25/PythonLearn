import os
import shutil
count2=1
def newfile():
    global count2  
    count=1
    choice=1
    while choice==1:
        if os.path.exists(filepath):
            if count==1:
                Title=input("Enter Title: ")
            else:
                pass
            text = input(f"Enter #{count} list item: ")
            listdot=str(count)+'. '
            textM=listdot+text
            with open(filepath ,'a+') as fp:
                if count==1:
                    fp.flush()
                    fp.write(Title+ '\n')
                    fp.write('             '+'\n')
                fp.write(textM+ '\n')
                fp.seek(0)
                print(fp.read())
            count += 1
            count2+=1
            choice = int(input("Enter 1 to continue and 0 to exit: "))
        else:
            print("File does not exist")
            break
    choice2=int(input("Enter 1 to create a copy of the file and 0 to exit: "))
    if choice2==1:
        dest=input("Enter destination: ")
        shutil.copy2(filepath,dest)
        print("File copied successfully")
    else:
        print("File not copied")

def modifyfile():
    global count2
    count=count2
    choice=1
    while choice==1:
        if os.path.exists(filepath):
            with open(filepath ,'a+') as fp:
                fp.seek(0)
                print(fp.read())
                text = input(f"Enter #{count} list item: ")
                listdot=str(count)+'. '
                textM=listdot+text
                fp.write(textM+ '\n')
                fp.seek(0)
                print(fp.read())
            count2 += 1
            choice = int(input("Enter 1 to continue and 0 to exit: "))
        else:
            print("File does not exist")
            break
    choice2=int(input("Enter 1 to create a copy of the file and 0 to exit: "))
    if choice2==1:
        dest=input("Enter destination: ")
        shutil.copy2(filepath,dest)
        print("File copied successfully")
    else:
        print("File not copied")

filepath = "D:\\College\\INT108\\Tests\\text.txt"
choice0=int(input("Enter 1 to create a new file, 2 to modify the old one and 0 to read the old one: "))

if choice0==1:
    newfile()
elif choice0==2:
    modifyfile()
else:
    with open(filepath) as fp:
        print(fp.read())
