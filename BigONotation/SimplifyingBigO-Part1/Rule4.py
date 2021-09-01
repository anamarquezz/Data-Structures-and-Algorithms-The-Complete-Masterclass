#Rule 4 - Consider diffenrent variable for different inputs

num_list = [1, 2, 3, 4, 5, 6, 7]
char_list = ['a','b','c','d','e']

def randomFunction(num_list, char_list):

    for num in num_list:
        print(num) #O(n)

    for char in char_list:
        print(char) #O(m)

print(randomFunction(num_list, char_list)) #O(n + m)

#####################################################

num_list = [1, 2, 3, 4, 5, 6, 7]

def randomFunction(num_list, char_list):

    for num in num_list:
        print(num) #O(n)
    
    for num in num_list:
        print(num) #O(n)


print(randomFunction(num_list, char_list)) #O(n + n)