employee_data =["raj","mmm","amit"]

for i in range(0,len(employee_data)):
    print(employee_data[i])

employee_data.append("jhon")
employee_data.insert(1,"amit")
#employee_data.clear()

print("count -->",employee_data.count("amit"))

print("popping...",employee_data.pop(1))


employee_data.remove("amit")

for i in employee_data:
    print(i)  



'''
print(employee_data[0])
print(employee_data[1])
print(employee_data[2])
'''    
