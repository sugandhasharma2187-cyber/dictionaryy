#nested dictionary
classroom={"student1":{"name":"tvisha","age":11,
                       "marks":[80,90,95,70,67]},
                       
            "student2":{"name":"tyla","age":12,
                        "marks":[67,50,100,80,90]},
            
            "student3":{"name":"saavi","age":11,
                        "marks":[60,90,50,60,80]}}
print(classroom,"\n")
print(f"the age of saavi is {classroom['student3']["age"]}\n")

print(f"the marks for tyla for math are {classroom['student2']["marks"][3]}")

#updating the marks of tvisha
classroom["student1"]["marks"][4]=76
print(f"the updated marks of tvisha are {classroom['student1']["marks"]}\n")

#retrieve student 3 info
print(classroom["student3"])

#change marks of student 2
classroom["student2"]["marks"][2]=90
print(classroom["student2"])