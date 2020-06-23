#full name using string concatenation
first_name = 'Mayank'
last_name = 'Srivastava'
full_name = first_name+' '+last_name
print(full_name)

#college name with address using string concatenation
clg_name = 'PSIT'
add = 'Kanpur'
x = clg_name+' '+add
print(x)

#marks of subjects with total marks and percentage
sub_1 = float(input("enter marks of sub_1:"))
sub_2 = float(input("enter marks of sub_2:"))
sub_3 = float(input("enter marks of sub_3:"))
sub_4 = float(input("enter marks of sub_4:"))
sub_5 = float(input("enter marks of sub_5:"))

total_marks = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
print(total_marks)

avg= (total_marks / 5)
print(avg)
