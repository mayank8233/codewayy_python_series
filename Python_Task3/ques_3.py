#Printing  the digitss from 1 to 10 except 7 and 3 by using for and while loop

# (1)   using the for loop

#defining a function using for loop!
def byForloop():
    for index in range(1,11):
        if(index == 3 or index == 7):
            continue
        else:
            print(index )
    
# (2) by using the while loop

#defining a function using while loop!
def byWhileloop() :    
    number=1
    while(number != 11):
        if(number == 3 or number == 7):
            number += 1
        else:
            print(number )
            number += 1

print("the numbers from 1 to 0 except 7 and 3 using the for loop!")
byForloop()
print("the numbers from 1 to 0 except 7 and 3 using the while loop!")
byWhileloop()
