# Handling the methods of using Lists:

#creating a list:
digits = [13,16,18,20,07,53,51]
print("The list of digits : ",digits)


# 1)by using the append() method to apend(add) a new element at the end of list:
numbers.append(45)
print("The list of digits after using append method: ",digits)


# 2)by using the insert() method to insert new element into list:
digits.insert(2,88)
print("The list of digits after using insert method: ",digits)


# 3)using remove() method to remove element:
digits.remove(20)
print("The list of digits after using remove method: ",digits)


# 4)using pop() method to delete last element:

#by passing the index in pop() method:
numbers.pop(3)
print("The list of digits after using pop method with index: ",digits)

#without passing the index in pop() method:
digits.pop()
print("The list of digits after using pop method without index: ",digits)


# 5)by using extend() method to combine elements to the list:
digits.extend([2,5,4])
print("The list of digits after using extend method: ",digits)


# 6)by using the min() method to get the minimum element:
digits1=min(digits)
print("The minimum digit from the list digits is: ",digits1)


# 7)by using the sum() method to get sum of all elements:
digits2=sum(digits)
print("The sum of all elements in the list digits is: ",digits2)
