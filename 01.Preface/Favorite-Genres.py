# creating genres dictionary to store data
genres = {
    "Action": 0, "Adventure": 0, "History": 0,
    "Comedy": 0, "Romance": 0, "Horror": 0,
}

# taking number of inputs
n = int(input())

# optimizing inputs to use in calculations
inputs = list()
for _ in range(n):
    a = input()
    a = a.split(" ")

    inputs.append(a)

# calculating genres sparsity
for i in range(len(inputs)):
    for j in range(3):
        genre = inputs[i][j+1]
        genres[genre] += 1

# sorting data
sorted_data = sorted(
    genres.items(),
    key=lambda x:(-x[1], x[0])
)

# printing results
for res in sorted_data:
    print(f"{res[0]} : {res[1]}")


# By Sina Kazemi
# https://github.com/sina96n