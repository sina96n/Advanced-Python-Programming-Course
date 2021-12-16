# creating dictionary to save words
dictionary = dict()

# number words to add their translation in dictionary
n = int(input())
for _ in range(n):
    a = input().split(" ")

    for i in range(3):
        dictionary[a[i+1]] = a[0]

# sentence that required to be translated
sentence = input().split(" ")

# finding translation from dictionary
translation = list()
for word in sentence:
    tr = [v for k,v in dictionary.items() if k == word]

    if tr == []:
        tr = word
    else:
        tr = tr[0]
    translation.append(tr)

# printing output
for i in translation:
    print(i, end=" ")


# By Sina Kazemi
# https://github.com/sina96n