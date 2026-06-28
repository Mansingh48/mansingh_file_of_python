import pandas as pd
import numpy as np

def grade(avg):
    if avg > 30  and avg <= 50:
        return  'B'
    elif avg > 50 and avg <= 70:
        return "B+"
    elif avg > 70 and avg <= 90:
        return 'A'
    elif avg > 90 and avg <  100:
        return "A++"
    else:
        return "back"
data = {
    "ID": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Ram","Raj","Jai","Mohan","Aman",
             "Ravi","Deepak","Sohan","Karan","Ajay"],

    "Maths": [85,30,90,87,78,55,99,34,92,76],
    "English": [78,52,88,70,81,60,84,40,91,73],
    "Python": [92,40,95,72,80,58,90,35,97,79],

    "Attendance": [95,70,98,85,90,75,96,60,99,88]
}

df = pd.DataFrame(data)

print(df)

df["avg"]= (
    df["Maths"]+ df["English"]  +df["Python"]
)/3

print(df)

df["Grade"] = df["avg"].apply(grade)
print(df)
df["maths_g"] = df["Maths"].apply(grade)
print(df)

to_performances = df[df["avg"] > 90]
print(to_performances)

df["top_guy"] = df["avg"].apply(
    lambda x: "yes" if x  > 90 else "no"
)
print(df)

low_attendence = df[df["Attendance"] > 75]
print("\n\n")
print(low_attendence)

df["lowAttendeces"] = df["Attendance"].apply(
    lambda x : "permited" if x > 75 else "not permited"
)
print(df)

list_not = df[df["Attendance"] < 75]
print(list_not)

shorted_by_avg = df.sort_values(
    by="avg", ascending=False, ignore_index=True
)
print(shorted_by_avg)

df.to_csv('student_performances.csv',
          index=  True)
df.to_excel("st_file.xlsx",index=True)



mid = np.mean(df["Maths"])

mid2  = np.mean(df["English"] + df["Maths"]+ df["Python"])
print(mid)
print(mid2)

max_value = np.max(df["Maths"])
min_value = np.min(df["Maths"])
print(max_value , "\nthe minimum value is :", min_value)

df["result_maths"] =  np.where(df["Maths"] >50 , "pass", "fail")
df["r_english"]= np.where(df["English"] > 50 ,"pass", "fail")
print(df)