# This program stores student name 
# and his/her courses and grades in a dict.
# The program them prints out his/her data.
# The number of course he/she has could change.
# In this example the data is hard coded.
# Author: Eret Haava

student = {
    "name": "Mary",
    "modules": [
        {
            "courseName": "Programming",
            "grade": 45
        },
        {
            "courseName": "History",
            "grade": 99
        }
    ]
}

print("Student: {}".format(student["name"]))

# modules in an array in the dict student
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))

