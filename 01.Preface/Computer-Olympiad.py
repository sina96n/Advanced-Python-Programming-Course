# creating a functon to modify names
def name_con(x) -> str:
    x = x.lower()
    x = x.capitalize()
    
    return x


# taking number of inputs
n = int(input())

# optimizing inputs to use in calculations
f_inputs = list()
m_inputs = list()
for _ in range(n):
    a = input()
    a = a.split(".")
    name = name_con(a[1])
    a[1] = name

    if a[0] == "f":
        f_inputs.append(a)
    elif a[0] == "m":
        m_inputs.append(a)

# sorting inputs
f_inputs = sorted(
    f_inputs,
    key=lambda x: x[1]
)
m_inputs = sorted(
    m_inputs,
    key=lambda x: x[1]
)

for female in f_inputs:
    print(f"{female[0]} {female[1]} {female[2]}")
for male in m_inputs:
    print(f"{male[0]} {male[1]} {male[2]}")


# By Sina Kazemi
# https://github.com/sina96n