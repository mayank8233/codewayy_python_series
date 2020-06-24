#Working with Tuples in Python

#Creation of Tuples
T1 = (3,8,9,11)
print(T1)

#Creating of Nested Tuples
T2 = (1,0,(15,7),5)
print(T2)

#Joining two Tuples
joinTuples = T1 + T2
print(joinTuples)

#Slicing a tuple
slicedTuple = joinTuples[1:3]
print(slicedTuple)

#Comparing the Tuples
T1 == T2

#Deleting the Tuples
del joinTuples
print("joinTuples deleted")

#len() Method
Length = len(T2)
print("Length of T2 is: ",Length)

#max() Method
Maximum = max(T1)
print("Maximum from T1 is: ",Maximum)

#min() Method
Minimum = min(T1)
print("Minimum from T1 is: ",Minimum)

#Index Method
Index = T2.index(1)
print(Index)

#Count() Method
Count = T1.count(2)
print("Count = ",Count)


#tuple() Method
strTuple = tuple("xyz")
print("Tuple from str 'xyz' is: ",strTuple)
