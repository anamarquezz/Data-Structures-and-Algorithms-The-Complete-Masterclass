student_list = ['Ana','Ale','Adriana','Santiago','Lidia']

def randomFunction(student_list):
    firs = student_list[0]
    total = 0
    new_list = []

    for student in student_list:
        total +=1
        new_list.append(student)

    print(new_list)
    return total

    
print(randomFunction(student_list))