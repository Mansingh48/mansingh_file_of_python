import numpy as np
import pandas as pd


def add_new(df, name, age , salary, score , department):
    total = salary + ( salary *0.10)
    df.loc[len(df)] = {
        "name" : name,
        "age" : age,
        "salary": salary,
        "score": score,      
        "total": total,
        "department" : department
    }
    return df


"""def id_maker(df):
    emp_id =[]
    id =100
    for i in range(len(df)):
        id +=  1
        emp_id.append(id)
    df.insert(0,  "emp_id",  emp_id)
    return  df
"""
def id_maker(df):
    df.insert(0 , "emp_id", range(100 , 100+len(df)))
    return  df



def add_by_user(df):
    name = input("enter your name  ")
    age= int(input("enter the age"))
    salary = int(input("enter your salary  "))
    score = int(input("enter your score  "))
    department = input("enter your deartpment  ")
    total = salary + (salary*0.10)

    df.loc[len(df)] = [name ,age, salary,department, score ,total    ]
    return df


data={
    "name": ["ram", "raj", None ,"shayam"],
    "age": [23,34,19, None ],
    "salary": [ None ,12000,18000,34000],
    "score": [89,43,69, None ]
}


df = pd.DataFrame(data)

df.insert(4, "extra_alonces", df["salary"] * 0.10 )

df.insert(5, "total", df["salary"] + df["extra_alonces"])

df.insert(3, "department", ["intern", "emp" , "hr", None ])
print()
print(df)
df.drop(columns="extra_alonces" , inplace=True)
print(df)

print(df.isnull(),"\n", df.isnull().sum())


# df["name"] = df["name"].fillna("unknown")
# df["department"] = df["department"].fillna("not assinged")

df.fillna({
    "name": "unknown",
    "age": 0,
    "salary" : 0,
    "score" : 0,
    "department": "not_assingned",
    "total": 0
} , inplace= True)

add_new(df,"mansigh", 19,  2000000,   90, "boss")
print(df)
# add_by_user(df)
print("\n\n\n")
print(df.loc[2])
print("\n\n", df.loc[1,"name"])
df["bonuss"] = 1000
df.loc[df["score"] > 70 , "bonuss"] =2500
id_maker(df)
print(df)