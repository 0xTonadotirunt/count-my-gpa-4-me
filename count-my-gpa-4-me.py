dict_of_grades = {"A+":(4.3,4.3), "A":(4.3,4), "A-":(4,3.7), "B+":(3.7,3.3), "B":(3.3,3), "B-":(3,2.7),"C+":(2.7,2.3), "C":(2.3,2), "C-":(2,1.7), "D+":(1.7,1.3), "D":(1.3,1), "F":(1,0)}
dictionary_of_user = {}
input_continue = "Y"
total = 0
while input_continue == "Y":
    name_of_comp = input("insert name of component: ")
    grade_of_comp = input("insert your score for the component: ")
    perc_of_comp = int(input("insert the percentage weightage: "))
    final_grade = dict_of_grades[grade_of_comp][1] * perc_of_comp/100
    total+= final_grade
    dictionary_of_user[name_of_comp] = grade_of_comp
    input_continue = input("do you want to input more values? [Y|N]")

print("-"*20)
for k,v in dictionary_of_user.items():
    print(f"|{k}:{v}|")

for k,v in dict_of_grades.items():
    if total < v[0] and total >= v[1]:
        print(f"Your final grade: {k}")

print(f"your score:{total}")
print("-"*20)
