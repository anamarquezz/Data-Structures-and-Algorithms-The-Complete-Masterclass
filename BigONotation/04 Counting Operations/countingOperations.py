student_list = ['Ana','Ale','Adriana','Santiago','Lidia'] #O(1)

def randomFunction(student_list):
    first = student_list[0] #O(1)
    total = 0 #O(1)
    new_list = [] #O(1)

    for student in student_list: 
        total +=1 #O(n)
        new_list.append(student) #O(n)

    print(new_list)#O(1)
    return total#O(1)

    
print(randomFunction(student_list))#O(6 + 2n) = O(n)