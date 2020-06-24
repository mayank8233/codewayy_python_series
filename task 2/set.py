#Working with the Sets in Python

#Intialising sets
alpha_set = {"a", "e", "i", "o", "u"}
print(alpha_set)

#Accesing the sets through loops
for index in alpha_set:
    print(index)
    
#Adding new item using add fucntion
alpha_set.add("g")
print(alpha_set)

#Adding multiple items using update fucntion
alpha_set.update(["a","b"])
print(alpha_set)

#getting the length
print(len(alpha_set))

#Removing items using discard fucntion
alpha_set.discard("i")
print(alpha_set)

#deleting using pop
Element = alpha_set.pop()
print(Element)
print(alpha_set)

#Using the union function to return the union of two sets
alpha_set2 = {"m"}
main_Set = alpha_set.union(alpha_set2)
print(main_Set)

#Using the difference function to return the union of two sets
main_Set2 = main_Set.union(alpha_set)
print(main_Set2)
