#the Program mentioned below contains marks and details.!

#func Name
def Name():
    Name = input("please Enter your good name:")
    print("your name is :",Name)

    
#func MyMarks
def Marks():
    dataStruct = int(input("Enter the obtained marks:"))
    compNtwrk = int(input("Enter the obtianed marks:"))
    OpSys = int(input("Enter the obtained marks:"))
    ArtIntel = int(input("Enter the obtained marks:"))
    global totMarks
    totMarks=dataStruct + compNtwrk + opSys + artIntel
    print("The Total marks are : ",totMarks)
    
#func Percentage
def Percnt():
    global score
    score=(totMarks)/4
    print("My percentage is : ",score,"%")

#func Grade  
def Grade():
    if(score>=95):
        print("Your Grade is :A")
    elif(score>=85 and score<=95):
       print("Your Grade is : B")
    elif(score>=75 and score<=85):
        print("Your Grade is : C")
    elif(score>=65 and score<=75):
        print("Your Grade is : D")
    else:
        print("Fail ")
      
#the function defined below displays all the details by calling the rest of the functions initialised above.!
def Details():
    Name()
    Marks()
    Percentage()
    Grade()

    Details()
