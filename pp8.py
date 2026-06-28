import numpy as np
import pandas as pd


"""1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Salary Analysis
7. Save Data
8. Exit """

def add_emp():
    n  = int(input("enter the number of employe's "))
    employe = []

    for i in range(n):
        print(f"\n\nenter the data of {i+1} employe ")
        name = input("enter the name of emp ")
        id_ = int(input("enter the ID' : "))
        age = int(input("enter the age of emp "))
        city = input("enter the city name ")
        salary = int(input("enter the salary of emp "))

        employe.append({
        "name": name,
        "id": id_,
        "age": age,
        "city": city,
        "salary": salary
    })
    return pd.DataFrame(employe)

def save(df):
    df.to_csv("biddu.csv")
    return df

def search(df):
    emp_id  = input("enter the emp id to search ")
    resutl = df[df["id"] ==  emp_id]
    if len(resutl)> 0:
        print(resutl)
    else:
        print("not found \n\n")

def delet(df):
    emp_id = int(input("enter the emp id to remove the emp "))
    if emp_id in df["id"].values:
        df =df[df["id"] != emp_id].reset_index(drop=True)
        print("DELETED FAHHHHHHHH")
    else:
        print(" not found ")
    return df

def add_new_emp(df):
    name = input("enter the name of emp ")
    id = int(input("enter the ID' : "))
    age = int(input("enter the age of emp "))
    city = input("enter the city name ")
    salary = int(input("enter the salary of emp "))
    df["bonus"] = 0
    df.loc[len(df)] ={
        "name": name,
        "id": id,
        "age": age,
        "city": city,
        "salary": salary,
        "bonus": 0
        
    }
    return df
def detail(df):
    mean = df["salary"].mean()
    mode = df["salary"].mode()
    median = df["salary"].median()
    print("mean of salary is :" , mean)
    print("median of salary is :" , median)
    print("mode of salary is :" , mode)


def bonas(df):
    df["bonus"] =0
    df.loc[
        (df["salary"] > 0) &
        (df["salary"] <30000) , "bonus"]  = df["salary"]* 0.10
    df.loc[
        (df["salary"]>=30000) &
        (df["salary"] < 60000) , "bonus"
    ] = df["salary"]* 0.30
    df.loc[
        (df["salary"] >= 60000)&
        (df["salary"]<100000) , "bonus"
    ] = df["salary"]*.40
    df.loc[
        df["salary"] >= 100000, "bonus"
    ] = df["salary"]*0.50

    return df
def total(df):
    df["total_salary"] = df["salary"]+ df["bonus"]
    return df
def menu():
    df = add_emp()
    while True:
        
        print("enter 1 for show data ")
        print("enter 2 for add   new emp ")
        print("enter 3 for adding bonus ")
        print("enter 4 for exit")
        print("enter 5 for detail of salary")
        print("enter 6 for total salary")
        print("enter 7 for FAHAAAAA(dl)")
        print("enter 8 for save the file")

        choise = int(input("enter you'r choise"))
        if choise == 1:
            print(df)
    
        elif choise == 2:
            df = add_new_emp(df)
            print()
            print(df)
        elif choise == 3 :
            df = bonas(df)
            print(df)
        elif choise == 4:
            break
        elif choise == 5 :
            df= detail(df)
        elif choise == 6:
            df = total(df)
            print(df)
        elif choise == 7 :
            df = delet(df)
            print(df)
        elif choise == 8:
            df = save(df)
        else:
            print("wrong number press again ")
menu()