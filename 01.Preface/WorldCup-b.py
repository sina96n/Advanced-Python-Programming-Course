# importing wraps for using decorators
from functools import wraps

# creating dictionaries for storing data
iran       = {"Name" : "Iran" , "wins" : 0 , "loses" : 0 , "draws" : 0 , 
              "goal difference" : 0 , "points" : 0}
spain      = {"Name" : "Spain" , "wins" : 0 , "loses" : 0 , "draws" : 0 , 
              "goal difference" : 0 , "points" : 0}
portugal   = {"Name" : "Portugal" , "wins" : 0 , "loses" : 0 , "draws" : 0 , 
              "goal difference" : 0 , "points" : 0}
maracco    = {"Name" : "Morocco" , "wins" : 0 , "loses" : 0 , "draws" : 0 , 
              "goal difference" : 0 , "points" : 0}

# decorator function for choosing turns
# we could use match-case with python 3.10
def counter(engine):
    wraps(engine)
    def wrapper(res, *args, **kwargs):

        i = kwargs["i"]

        if i == 1:
            t1 = iran
            t2 = spain
        elif i == 2:
            t1 = iran
            t2 = portugal
        elif i == 3:
            t1 = iran
            t2 = maracco
        elif i == 4:
            t1 = spain
            t2 = portugal
        elif i == 5:
            t1 = spain
            t2 = maracco
        elif i == 6:
            t1 = portugal
            t2 = maracco
        
        return engine(res, t_1=t1, t_2=t2)
    
    return wrapper

# main function to do calculations
@counter
def engine(res, *args, **kwargs):

    t_1 = kwargs["t_1"]
    t_2 = kwargs["t_2"]
    # converting inputs to integer
    res = list(map(int, res))

    a_score = res[0]
    b_score = res[1]

    g_diff_1 = a_score - b_score
    t_1["goal difference"] += g_diff_1
    g_diff_2 = b_score - a_score
    t_2["goal difference"] += g_diff_2

    if a_score > b_score:
        t_1["wins"]   += 1
        t_1["points"] += 3
        t_2["loses"]  += 1
    elif b_score > a_score:
        t_2["wins"]   += 1
        t_2["points"] += 3
        t_1["loses"]  += 1
    elif a_score == b_score:
        t_1["draws"]  += 1
        t_1["points"] += 1
        t_2["draws"]  += 1
        t_2["points"] += 1


results = list()

# getting scores
for _ in range(6):
    results.append(input())

# splitting inputs for calculations
count = 1
for res in results:
    res = res.split("-")
    engine(res, i=count)
    count += 1

# sorting final results
teams = [iran, spain, portugal, maracco]
order = {
    "points" : 0,
    "wins" : 0,
    "Name" : 0,
}
# lambda x: (x["points"], x["wins"], x["Name"])
teams = sorted(
    teams,
    key=lambda x: (-x["points"], -x["wins"], x["Name"]),
)

# printing output
for team in teams:
    values = [val for val in team.values()]
    print(f"{values[0]}  wins:{values[1]} , loses:{values[2]} , draws:{values[3]} , goal difference:{values[4]} , points:{values[5]}")


# By Sina Kazemi
# https://github.com/sina96n