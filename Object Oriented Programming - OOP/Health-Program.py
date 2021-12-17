# creating School class to hold class A and B 
class School():
    count = 0
    def __init__(self, name, n) -> None:
        # initializing with name of class and number of atandees
        self.name = name
        self.n = n

        # students list
        self.students = list() 
        
        # number of classes
        School.count += 0

    # method to students into class
    def add_student(self, info):
        student = info
        self.students.append(student)


    def get_age_average(self):
        ages = list()
        for student in self.students:
            ages.append(student[0])

        self.age_average = sum(ages) / len(ages)


    def get_height_average(self):
        heights = list()
        for student in self.students:
            heights.append(student[1])

        self.heights_average = sum(heights) / len(heights)


    def get_weight_average(self):
        weights = list()
        for student in self.students:
            weights.append(student[2])

        self.weights_average = sum(weights) / len(weights)

    
    def __str__(self) -> str:
        return f"Class {self.name} with {self.n} students."


# GETTING CLASS A INPUPT
n = int(input())
A = School("A", n)

ages = input().split()
heights = input().split()
weights = input().split()

students = list(zip(ages, heights, weights))
for i in range(n):
    student = students[i]
    student = list(map(int, student))
    # adding extracted student to the class
    A.add_student(student) 


# GETTING CLASS B INPUPT
n = int(input())
B = School("B", n)

ages = input().split()
heights = input().split()
weights = input().split()

students = list(zip(ages, heights, weights))
for i in range(n):
    student = students[i]
    student = list(map(int, student))
    # adding extracted student to the class
    B.add_student(student) 

# Claculating average age, height and weight for class A
A.get_age_average()
A.get_height_average()
A.get_weight_average()

# # Claculating average age, height and weight for class B
B.get_age_average()
B.get_height_average()
B.get_weight_average()

# preparing outputs
A_info = [A.age_average, A.heights_average, A.weights_average]
B_info = [B.age_average, B.heights_average, B.weights_average]

# printing results
for i in range(3):
    print(A_info[i])
for i in range(3):
    print(B_info[i])

output = sorted(
    [A_info, B_info],
    key=lambda x: (-x[1], x[2])
)

# printing the healthier class
if (A_info[1] == B_info[1]) and (A_info[2] == B_info[2]):
    print("Same")

elif output[0] == A_info:
    print("A")

elif output[0] == B_info:
    print("B")


# By Sina Kazemi
# https://github.com/sina96n