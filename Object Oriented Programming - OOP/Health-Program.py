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

        self.age_average = "{:.1f}".format(sum(ages) / len(ages))
        print(self.age_average)


    def get_height_average(self):
        heights = list()
        for student in self.students:
            heights.append(student[1])

        self.heights_average = "{:.1f}".format(sum(heights) / len(heights))
        print(self.heights_average)
        

    def get_weight_average(self):
        weights = list()
        for student in self.students:
            weights.append(student[0])

        self.weights_average = "{:.1f}".format(sum(weights) / len(weights))
        print(self.weights_average)