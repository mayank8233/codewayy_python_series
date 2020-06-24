# 7 ways of handling the dictionary data type.!


# creating a dictionary:
vowels = {"a":"Apple","e":"Elephant","i":"Indigo","o":"Orange","u":"umbrella"}
print("The dictionary of vowels : ",vowels)


# 1)by using the get() method to get value:
get_vowel=vowels.get("e")
print("value for the 'e' key is: ",get_vowel)



# 2)by using  the keys() method to get keys:
keys = vowels.keys()
print("keys: ",keys)


# 3)by using the len() method to find the length:
length = len(vowels)
print("The length of the vowels dictionary is: ",length)


# 4)by using the values() method to get all the values:
values = vowels.values()
print("values: ",values)


# 5)by using the items() method to get all the items of dictionary:
items = vowels.items()
print("Items: ",items)



# 6)by using the pop() method to delete last element:
vowels.pop("o")
print("The vowels dictionary after performing a pop('o') opearation: ",vowels)


# 7)by using the copy() method to copy the given dictionary into another:
vowels_new = vowels.copy()
print("The new copy of vowels dictionary is: ",vowels_new)
