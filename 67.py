file=open("D:\\College\\INT108\\Tests\\textfile.txt","w")
num=int(input("Enter number of lines to write:"))
for i in range(1,num+1):
    line=input("Enter line: ")
    file.write(str(i)+". "+line+"\n")
file.close()
c1=int(input("Enter 1 to read the file,2 to delete the contents, 3 to seek, 4 to count number of characters, 5 for number of words, 6 for number of vowels: "))
if c1==1:
    file=open("D:\\College\\INT108\\Tests\\textfile.txt","r")
    print(file.read())
    file.close()
elif c1==2:
    file=open("D:\\College\\INT108\\Tests\\textfile.txt","w")
    file.write("")
    file.close()
elif c1==3:
    file=open("D:\\College\\INT108\\Tests\\textfile.txt","r")
    seek_value=int(input("Enter the value to seek: "))  
    file.seek(seek_value)
    print(file.read())
    file.close()
elif c1==4:
    count=0
    file=open("D:\\College\\INT108\\Tests\\textfile.txt","r")
    for line in file:
        for char in line:
            count+=1
    print("Number of characters in the file: ",count)
    file.close()
elif c1==5:
    count=0
    file=open("D:\\College\\INT108\\Tests\\textfile.txt","r")
    for line in file:
        for word in line.split():
            count+=1
    print("Number of words in the file: ",count-1)
    file.close()
elif c1==6:
    count=0
    vowels="aeiouAEIOU"
    file=open("D:\\College\\INT108\\Tests\\textfile.txt","r")
    for line in file:
        for char in line:
            if char in vowels:
                count+=1
    print("Number of vowels in the file: ",count)
    file.close()