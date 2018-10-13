#q.no.1
dict={}
for i in range (int(input("Enter the key-value pairs you want to input:"))):
    dict[i]=i
n=int(input("Enter the value for which the key you want to search:"))
for key in dict.keys():
    if dict[key]==n:
        print(key)
    else:
        print("key not found!!! Error")
print("total elements present are:",dict[i])

#q.no.2
students={
          "danish":{"networks":76,"python":56,"sexeducation":80,"java":40},
          "rohit":{"networks":86,"python":96,"sexeducation":90}
          }
stu_name=input("Enter the name of student you want to search:").title()
if stu_name in students:
    print("stu_name")
    for key,value in students[stu_name].items():
        print(key,value)
else:
    print("No such student in the list as you mentioned")

