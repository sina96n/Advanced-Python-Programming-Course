class School():
    count = 0
    def __init__(self, name, n) -> None:
        self.name = name
        self.n = n

        self.students = list() 
        
        School.count += 0

    def add_student(self, info):
        student = info
        self.students.append(student)


    def get_age_average(self):
        ages = list()
        for student in self.students:
            ages.append(student[0])

        self.age_average = round(sum(ages) / len(ages), 1)


    def get_height_average(self):
        heights = list()
        for student in self.students:
            heights.append(student[1])

        self.heights_average = round(sum(heights) / len(heights), 1)


    def get_weight_average(self):
        weights = list()
        for student in self.students:
            weights.append(student[0])

        self.weights_average = round(sum(weights) / len(weights), 1)


n = int(input())
A = School("A", n)

inputs = input().split()
inputs = list(map(int, inputs))

for i in range(n):
    student = inputs[3*i:3*i+2]
    A.add_student(student)


n = int(input())
B = School("B", n)

inputs = input().split()
inputs = list(map(int, inputs))

for i in range(n):
    student = inputs[3*i:3*i+2]
    B.add_student(student)


A.get_age_average()
A.get_height_average()
A.get_weight_average()

B.get_age_average()
B.get_height_average()
B.get_weight_average()

A_info = [A.age_average, A.heights_average, A.weights_average]
B_info = [B.age_average, B.heights_average, B.weights_average]

output = [A_info, B_info].sort(
    key=lambda x: (-x[1], x[2])
)

for i in output:
    for j in range(3):
        print(i[j])

if (A_info[1] == B_info[1]) and (A_info[2] == B_info[2]):
    print("Same")